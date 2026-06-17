# Linux Essentials for PAM

A sysadmin's bridge into Privileged Access Management (PAM) starts with Linux,
because the **WALLIX Bastion** is a **Debian-based GNU/Linux appliance**. It boots
Linux, runs Linux services (`syslog-ng`, `redemption`, MariaDB), proxies **Secure
Shell (SSH)** connections, and exposes a Linux command-line interface (CLI) that the
**WCE-P** (WALLIX Certified Expert – PAM) certification explicitly requires you to
know. This file teaches the Linux building blocks you will lean on every day and ties
each one to *how Bastion uses it*.

> **Acronym warning (read this twice):** In the Linux world, **PAM = Pluggable
> Authentication Modules** — a local authentication framework (`/etc/pam.d/`). In *our*
> world, **PAM = Privileged Access Management** — the WALLIX product category. Same
> three letters, completely different things. This file flags which is meant every
> time. See [../reference/acronyms.md](../reference/acronyms.md).

## Learning objectives

By the end of this file you should be able to:

- Explain SSH server vs. client, and walk through **key-based authentication**.
- Read and edit `sshd_config` and understand `known_hosts`.
- Use `sudo` and `su` and explain the difference (privilege escalation on Linux).
- Manage Linux **users, groups, and file permissions**.
- Describe **systemd** services and how to inspect them.
- Find logs via **journald** and `/var/log`.
- Disambiguate **Linux PAM** (Pluggable Authentication Modules) from **WALLIX PAM**
  (Privileged Access Management).
- Map each concept to a concrete behaviour of the WALLIX Bastion appliance.

---

## 1. SSH — Secure Shell

**SSH (Secure Shell)** is an encrypted protocol (default **TCP port 22**) for remote
command-line login and tunnelling. It replaced insecure **Telnet** and **rlogin**
(plaintext). On Linux it has two halves:

| Half | Program (OpenSSH) | Role |
|------|-------------------|------|
| **Server** | `sshd` (SSH daemon) | Listens on port 22, authenticates clients, opens shells |
| **Client** | `ssh` | Initiates the connection from your workstation |

```bash
# Client: connect to a server
ssh alice@server.example.com

# Client: connect on a non-default port
ssh -p 2222 alice@server.example.com
```

### Why this matters for Bastion

The WALLIX Bastion **Session Manager** is, at heart, an **SSH proxy** (plus RDP, VNC,
Telnet, etc.). The administrator's `ssh` client connects to the *Bastion*, not the
target. The Bastion authenticates the admin, then opens a *second* SSH connection to
the real target on the admin's behalf, injecting the vaulted credential. The admin
never learns the target password. Two SSH legs, one broker in the middle:

```
+-----------+        SSH leg 1         +-----------+        SSH leg 2         +-----------+
|           |  port 22 (admin login)   |           |  port 22 (vaulted creds) |           |
|   Admin   | -----------------------> |  WALLIX   | -----------------------> |  Target   |
|  ssh cli  |   admin's own identity   |  Bastion  |  injected target account |  server   |
|           | <----------------------- |  (proxy)  | <----------------------- |           |
+-----------+    recorded + audited    +-----------+                          +-----------+
```

### SSH key-based authentication

Passwords can be guessed or phished. **Public-key authentication** uses an
**asymmetric key pair**: a **private key** that never leaves the client, and a
**public key** placed on the server. (See key types and crypto in
[cryptography-and-pki.md](cryptography-and-pki.md).)

```bash
# 1. Generate a key pair on the CLIENT (Ed25519 recommended)
ssh-keygen -t ed25519 -C "alice@workstation"
#  -> creates ~/.ssh/id_ed25519       (PRIVATE key — keep secret)
#  -> creates ~/.ssh/id_ed25519.pub   (PUBLIC key — safe to share)

# 2. Install the PUBLIC key on the SERVER
ssh-copy-id alice@server.example.com
#  -> appends the .pub line to /home/alice/.ssh/authorized_keys on the server

# 3. Log in with no password
ssh alice@server.example.com
```

#### FLOW: SSH public-key authentication handshake

This is the exchange that proves "I hold the private key" *without ever sending it*.
After the encrypted transport channel is set up (Diffie-Hellman key exchange), the
authentication step runs:

```
   CLIENT (ssh)                                          SERVER (sshd)
   private key id_ed25519                       authorized_keys (your public key)
        |                                                      |
        |   (1) "I want to log in as alice"                    |
        | ---------------------------------------------------> |
        |                                                      |
        |        (2) Is alice's public key in                  |
        |            authorized_keys?  YES.                    |
        |            Server sends a random CHALLENGE            |
        | <--------------------------------------------------- |
        |                                                      |
        |   (3) Sign the challenge with the PRIVATE key         |
        |       (the private key never leaves the client)      |
        | ---------------------------------------------------> |
        |                                                      |
        |        (4) Verify the signature using the            |
        |            stored PUBLIC key. Valid?                  |
        |            -> grant shell session                    |
        | <--------------------------------------------------- |
        |                                                      |
        |   (5) Encrypted interactive shell session            |
        | <==================================================> |
```

**Key idea:** the private key is used to *sign* a challenge; the server *verifies* with
the public key. The secret material never crosses the wire.

#### `sshd_config` — the server's rule book

`/etc/ssh/sshd_config` controls how `sshd` behaves. Common hardening directives:

```ini
# /etc/ssh/sshd_config
Port 22
PermitRootLogin no              # never allow direct root SSH login
PasswordAuthentication no       # force key-based auth only
PubkeyAuthentication yes        # enable public-key auth
AllowGroups ssh-users           # only members of this group may connect
```

Reload after editing: `sudo systemctl reload sshd` (see systemd below).

> **Bastion tie-in:** Bastion **rotates** the SSH keys it stores for target accounts
> and supports SSH **sub-protocols** (shell, SCP, SFTP, X11, direct-TCPIP) that you can
> allow or deny per authorization. Understanding `sshd_config` on the *target* side
> helps you grasp what Bastion is negotiating on the second SSH leg.

#### `known_hosts` — trusting server identities

The first time you SSH to a host, the client stores the server's **host public key** in
`~/.ssh/known_hosts`. On later connections the client checks the host key matches — if
it changed, SSH warns of a possible **man-in-the-middle (MITM)** attack.

```bash
# View / clean a stale entry after a server is rebuilt
ssh-keygen -R server.example.com
```

> **Bastion tie-in:** Bastion maintains its own known-hosts trust for the *target* leg
> and can pin/verify target host keys, protecting the Bastion→target hop from MITM.

---

## 2. Privilege escalation on Linux — `su` and `sudo`

PAM (Privileged Access Management) is *all about* who may become privileged. Linux gives
you two native mechanisms:

| Command | What it does | Typical use |
|---------|--------------|-------------|
| `su` (substitute user) | Opens a shell *as another user* (often `root`); asks for the **target user's** password | `su -` to become root |
| `sudo` (superuser do) | Runs **one command** as another user (default root); asks for **your own** password; governed by `/etc/sudoers` | `sudo systemctl restart sshd` |

```bash
su -                       # become root (needs root's password)
sudo apt update            # run one command as root (needs YOUR password)
sudo -u postgres psql      # run as a specific service user
```

`sudo` is preferred because it is **auditable and granular** — `/etc/sudoers` (edited
with `visudo`) says exactly which user may run which command as whom:

```sudoers
# /etc/sudoers  — alice may restart only the web service, as root, no password
alice  ALL=(root) NOPASSWD: /usr/bin/systemctl restart nginx
```

> **Bastion tie-in:** Bastion has **scenario accounts** that automate `su`/`sudo` at the
> start of an SSH session — e.g., log in as an unprivileged account, then auto-elevate
> to root using a vaulted password the user never sees. This is least-privilege +
> credential injection in action. (Endpoint-side elevation is BestSafe's job; see the
> [product portfolio](../docs/00-overview/product-portfolio.md#4-wallix-bestsafe--endpoint-privilege-management-epm).)

---

## 3. Users, groups, and file permissions

### Users and groups

- A **user** has a numeric **UID (User ID)**; defined in `/etc/passwd`.
- A **group** has a numeric **GID (Group ID)**; defined in `/etc/group`.
- Password hashes live in `/etc/shadow` (root-readable only).
- A user has one **primary group** and any number of **supplementary groups**.

```bash
id alice                       # show alice's UID, GID, groups
sudo useradd -m -s /bin/bash bob   # create user bob with a home dir + bash shell
sudo usermod -aG sudo bob          # add bob to the 'sudo' group (grant sudo rights)
groups bob                     # list bob's groups
```

### File permissions (the `rwx` model)

Every file/directory has an **owner**, a **group**, and three permission triplets:

```
   -    rwx    r-x    r--
   ^     ^      ^      ^
  type owner  group  others
       (u)     (g)    (o)

   r = read (4)   w = write (2)   x = execute (1)
```

```bash
ls -l id_ed25519
# -rw-------  1 alice alice 411 Jun 17 10:00 id_ed25519   (mode 600)

chmod 600 ~/.ssh/id_ed25519    # private key MUST be owner-only or ssh refuses it
chmod 644 ~/.ssh/id_ed25519.pub
chown alice:alice file.txt     # change owner and group
```

`chmod 600` = owner read+write (6), group nothing (0), others nothing (0). SSH will
**refuse to use a private key** that other users can read — a classic first-day gotcha.

> **Bastion tie-in:** The Bastion appliance is Linux; understanding owner/group/`rwx`
> lets you read appliance file listings, fix key-file permissions in labs, and reason
> about why `sshd` rejects a misconfigured key.

---

## 4. systemd — services, units, and the service manager

**systemd** is the init system and service manager on Debian (and most modern Linux).
It starts services at boot and supervises them. Each service is a **unit**
(e.g., `sshd.service`).

```bash
systemctl status sshd          # is the SSH daemon running?
sudo systemctl start  sshd     # start it
sudo systemctl stop   sshd     # stop it
sudo systemctl restart sshd    # restart
sudo systemctl reload sshd     # re-read config without dropping connections
sudo systemctl enable sshd     # start automatically at boot
systemctl list-units --type=service   # all active services
```

> **Bastion tie-in:** Bastion's internal components run as services/processes —
> `redemption` (the RDP proxy engine), `wabgui` (admin GUI), `wabrestapi` (REST API),
> MariaDB, `syslog-ng`, `wabwatchdog`, etc. (per the
> [product portfolio](../docs/00-overview/product-portfolio.md#architecture-deployment-ha-integrations)).
> WCE-P troubleshooting often means checking whether one of these services is healthy —
> exactly the `systemctl status` muscle memory you build here.

---

## 5. Linux logging — journald and `/var/log`

Logs are the auditor's and troubleshooter's best friend. Two layers coexist on Debian:

| Layer | Where | Read with |
|-------|-------|-----------|
| **journald** (systemd journal) | binary journal | `journalctl` |
| Classic text logs | `/var/log/*` (e.g., `auth.log`, `syslog`) | `less`, `grep`, `tail` |

```bash
journalctl -u sshd                 # all log lines for the sshd service
journalctl -u sshd -f              # follow live (like tail -f)
journalctl --since "1 hour ago"    # time-bounded
sudo tail -f /var/log/auth.log     # live authentication events (logins, sudo, su)
grep "Failed password" /var/log/auth.log   # spot brute-force attempts
```

`/var/log/auth.log` records every login, `sudo`, and `su` — the raw material of access
auditing.

> **Bastion tie-in:** Bastion centralizes and **forwards logs via Syslog**
> (`syslog-ng`, **UDP/TCP 514**) to a **SIEM (Security Information and Event
> Management)** platform, and records full session video/transcripts on top. The Linux
> logging skills here are the foundation for understanding Bastion's audit pipeline.
> See protocol details in
> [networking-and-protocols.md](networking-and-protocols.md).

---

## 6. The two PAMs — never confuse them again

| | **Linux PAM** | **WALLIX PAM** |
|---|---|---|
| Stands for | **P**luggable **A**uthentication **M**odules | **P**rivileged **A**ccess **M**anagement |
| What it is | A local Linux framework that lets programs (login, sudo, sshd) plug in auth methods | A security product category / WALLIX Bastion |
| Lives in | `/etc/pam.d/`, `/lib/.../security/*.so` | A network appliance brokering privileged sessions |
| Scope | One host's authentication logic | Enterprise-wide privileged access control |
| Example | `pam_unix.so` checks `/etc/shadow`; `pam_google_authenticator.so` adds TOTP | Bastion vaults a root password and records the session |

Both can appear in the same sentence: *"We configured the target's **Linux PAM** stack
to require MFA, and put the host behind **WALLIX PAM** (Bastion) for session
recording."* When in doubt, expand the acronym.

```
   /etc/pam.d/sshd  (Linux PAM stack)            WALLIX Bastion (WALLIX PAM)
   +---------------------------+                 +---------------------------+
   |  pam_unix.so   (password) |                 |  vaults credentials       |
   |  pam_..._otp   (2nd factor)|   <-- local --> |  brokers + records session|
   |  pam_limits.so (resource) |   on ONE host    |  across the ENTERPRISE    |
   +---------------------------+                 +---------------------------+
```

---

## How this maps to the certifications

- **WCA-P / WCP-P** (Administrator / Professional): expect SSH, RDP, proxy concepts,
  and "Linux fundamentals" as stated prerequisites
  (see [pam-bastion track](../docs/pam-bastion/README.md)).
- **WCE-P** (Expert): explicitly requires **GNU/Linux command-line** knowledge — the
  `systemctl`, `journalctl`, permissions, and SSH-config skills above are directly
  exercised in advanced deployment and troubleshooting labs
  (see [wce-p-expert.md](../docs/pam-bastion/wce-p-expert.md)).

---

## Sources

- OpenSSH manual pages (`ssh`, `sshd`, `sshd_config`, `ssh-keygen`): https://man.openbsd.org/sshd_config
- RFC 4251 — The Secure Shell (SSH) Protocol Architecture: https://www.rfc-editor.org/rfc/rfc4251
- RFC 4252 — The Secure Shell (SSH) Authentication Protocol (public-key method): https://www.rfc-editor.org/rfc/rfc4252
- Linux PAM (Pluggable Authentication Modules) documentation: https://www.man7.org/linux/man-pages/man8/pam.8.html
- `sudo` / `sudoers` manual: https://www.sudo.ws/docs/man/sudoers.man/
- systemd / `systemctl` documentation: https://www.freedesktop.org/software/systemd/man/latest/systemctl.html
- `journalctl` documentation: https://www.freedesktop.org/software/systemd/man/latest/journalctl.html
- WALLIX Bastion architecture/components: [product-portfolio.md](../docs/00-overview/product-portfolio.md) (compiled from WALLIX Bastion 12.0.2 Deployment Guide and 12.3.2 Administration Guide)
