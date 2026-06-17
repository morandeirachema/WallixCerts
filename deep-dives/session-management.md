# WALLIX Bastion Session Manager — Protocols, Recording, Monitoring, Approvals

The **Session Manager** is the half of WALLIX Bastion that *brokers, proxies, controls, records, and audits* live privileged connections. It is licence-gated by the **Sessions** right on an authorization (see [./bastion-data-model.md](./bastion-data-model.md#3-the-authorization-object-in-detail)). This file is the deep dive on **how a session is opened, governed protocol-by-protocol, recorded encrypted, watched in real time, shared, and gated by approval workflows.**

For where the proxy services run (the `redemption` RDP proxy, SSH proxy, `wallixsession`) see [./bastion-architecture.md](./bastion-architecture.md#4-internal-components--services). For credential injection on the back leg see [./secrets-and-password-management.md](./secrets-and-password-management.md). Portfolio summary: [product portfolio](../docs/00-overview/product-portfolio.md#session-management). Acronyms: [../reference/acronyms.md](../reference/acronyms.md).

> **Served document version:** WALLIX Bastion **12.3.2** *Functional Administration Guide*.

---

## Key points

- Supported proxy **protocols:** SSH (with SFTP/sub-systems), TELNET, RLOGIN, RDP, VNC, **RAW TCP/IP** (Universal Tunneling / UT), **WEBAPP**, and standard applications / RemoteApp via a Windows jump server.
- **Sub-protocols** are authorization-gated channels (e.g. `SSH_SCP_UP`, `RDP_CLIPBOARD_DOWN`, `RDP_DRIVE`) — fine-grained "what can happen *inside* the session."
- A **connection policy** governs the back-leg (Bastion→target) behaviour per protocol; built-in policies include hardened **CCN** and **SOG-IS CES 1.3** variants.
- **Recordings are encrypted so only the originating Bastion can replay them**; RDP/SSH captured as video, textual SSH as transcript.
- The **Session Probe** (RDP/Windows only) collects rich metadata and **pauses keystroke capture on password fields / UAC windows**.
- **Restriction rules** (`kill` / `notify`) match regex on client-to-server data; for RDP they support **OCR of window titles** via `$ocr:` / `$kbd:` prefixes.
- Real-time control: **4 eyes** (watch only) vs **4 hands** (take control); plus **Session Invite** of an external guest into RDP/VNC.
- **Approval workflows** add quorum-based gating with separate rules inside vs outside the time frame, mandatory comment/ticket, timeout, and single-connection.

---

## 1. Protocols and sub-protocols

The Bastion proxies these protocols (§5.1, §12, §13.2):

| Primary protocol | Notes | Primary connection used |
|---|---|---|
| **SSH** (+ sub-systems) | Shell, remote command, SCP, SFTP, X11, TCP/Unix-socket forwarding, agent forwarding. | SSH |
| **TELNET**, **RLOGIN** | Legacy; credential automation needs a **connection scenario**. | SSH (proxy) |
| **RDP** | Full Windows desktop; hosts the **Session Probe**. | RDP |
| **VNC** | Can also tunnel over SSH. | RDP (or SSH tunnel) |
| **RAW TCP/IP — Universal Tunneling (UT)** | Forwards arbitrary local TCP ports to a target (e.g. industrial protocols); SSH proxy provides the port forwarding and monitors it. | SSH |
| **WEBAPP** | Web applications (via Web Session Manager / RBI). | RDP/HTML5 |
| **Standard application / RemoteApp** | Apps published on a Windows jump server. | RDP |

**Sub-protocols are the authorization parameters** that allow/forbid specific actions *inside* the session. Selected examples from §13.2:

**SSH target**

| Action | Authorization sub-protocol(s) |
|---|---|
| Start a shell session | `SSH_SHELL_SESSION` |
| Execute a remote command | `SSH_REMOTE_COMMAND` |
| X11 graphical forwarding | `SSH_SHELL_SESSION` (or `SSH_REMOTE_COMMAND`) `+ SSH_X11` |
| SCP file transfer | `SSH_SCP_UP` (to target) / `SSH_SCP_DOWN` (from target) |
| SFTP file transfer | `SFTP_SESSION` |
| Agent forwarding | `… + SSH_AUTH_AGENT` |
| TCP port forwarding | `SSH_DIRECT_TCPIP` / `SSH_SHELL_SESSION + SSH_REVERSE_TCPIP` |
| Unix-socket forwarding | `SSH_DIRECT_UNIXSOCK` / `… + SSH_REVERSE_UNIXSOCK` |

> **Security note (verbatim):** WALLIX recommends allowing `SSH_SCP_UP`/`SSH_SCP_DOWN` only alongside `SSH_SHELL_SESSION`, because SCP allows command injection (**CVE-2020-15778**); prefer `SFTP_SESSION` for transfer without shell. Also: by default only **one session channel** can be open per SSH connection unless the admin allows several. *(External reference: [CVE-2020-15778](https://nvd.nist.gov/vuln/detail/CVE-2020-15778).)*

**RDP target** (any RDP action first needs the session-start right `RDP`)

| Action | Sub-protocol(s) |
|---|---|
| Clipboard text | `RDP_CLIPBOARD_UP` / `RDP_CLIPBOARD_DOWN` |
| File transfer (clipboard) | `RDP_CLIPBOARD_FILE` + `RDP_CLIPBOARD_UP`/`_DOWN` |
| Local printer | `RDP_PRINTER` |
| Local COM port | `RDP_COM_PORT` |
| Shared/redirected drive | `RDP_DRIVE` |
| Smart card | `RDP_SMARTCARD` |
| Audio out / mic in | `RDP_AUDIO_OUTPUT` / `RDP_AUDIO_INPUT` |

**Other:** `VNC`, `TELNET`, `RLOGIN`, `RAWTCPIP`, `WEBAPP` are each a single start-the-session parameter (with the primary connection noted: VNC over RDP; TELNET/RLOGIN/RAWTCPIP over SSH).

---

## 2. Connection policies

A **connection policy** = the rules applied on the **secondary connection** (Bastion→target) for a given protocol. Each target's service references one. You can clone and customise them.

**Built-in policies (cannot be deleted):** `RAWTCPIP`, `RDP`, `RDP-ccn`, `RDP-sogisces_1.3_2030`, `RLOGIN`, `SSH`, `SSH-ccn`, `SSH-sogisces_1.3_2030`, `TELNET`, `VNC`, `WEBAPP`.

> WALLIX recommends the **CCN-STIC** or **SOG-IS CES 1.3** (valid to 2030) policies "wherever applicable" for high cryptographic assurance.

The policy is where the **back-leg authentication methods** are enabled and ordered — `PASSWORD_VAULT`, `PASSWORD_MAPPING`, `PASSWORD_INTERACTIVE`, `PUBKEY_AGENT_FORWARDING`, `KERBEROS_FORWARDING`, etc. — and where **Session Probe** and many RDP/SSH knobs live (see §1 of the data-model file for how these tie to mapping modes).

---

## 3. Session connection sequence

```
 CLIENT                         BASTION                         TARGET
   |  1. open SSH/RDP/HTTPS (front leg)                            |
   |------------------------------------>|                         |
   |  2. authenticate user (+MFA)        |                         |
   |<-----------------------------------|                         |
   |        [evaluate AUTHORIZATION: user grp -> target grp,       |
   |         Sessions right? protocol/sub-proto allowed?           |
   |         time frame? approval needed?]   (see data-model file) |
   |  3. if approval required -> request -> wait for quorum        |
   |                                     |                         |
   |                                     |  4. secondary connection (back leg)
   |                                     |     obtain credential:  |
   |                                     |     PASSWORD_VAULT /     |
   |                                     |     MAPPING / INTERACTIVE|
   |                                     |------------------------>|
   |                                     |  5. session established  |
   |  6. proxied traffic <==============>|<=======================>|
   |                                     |   RECORD (video/transcript)
   |                                     |   Session Probe metadata (RDP)
   |                                     |   restriction rules (kill/notify, OCR)
   |                                     |   real-time monitoring (4-eyes/4-hands)
   |                                     |   stream events -> SIEM (syslog-ng)
   |  7. disconnect / kill / approval-end -> session closed, recording sealed
```

---

## 4. Session recording and the audit pipeline

> Glossary: *Session recording* = "Recording of RDP or SSH sessions … viewed by auditors through a session video player embedded in WALLIX Bastion. **Their encryption allows only the WALLIX Bastion instances which created them to access these recordings.**"

Key facts:

- **Per-authorization toggle** ("Session recording" on the authorization). *Type depends on protocol.*
- **Video** for RDP and graphical sessions; **transcript** for textual SSH (keystrokes/output).
- **Encryption is Bastion-bound** — recordings can be replayed **only by the originating Bastion** (a direct consequence of the per-node, non-replicated audit tables described in [architecture/HA](./bastion-architecture.md#6-high-availability-and-scaling)). Cross-Bastion replay is brokered centrally by **Access Manager** (Elasticsearch-backed search), not by copying files.
- **Auditors can watch current SSH sessions live even when recording is OFF** in the authorization (explicit warning in §13).
- Events/metadata are forwarded to a **SIEM via `syslog-ng`** for correlation.

```
  LIVE SESSION ──► proxy captures ──► VIDEO (RDP) / TRANSCRIPT (SSH)
        │                              encrypted, Bastion-bound, on /var/wab (LVM)
        ├──► Session Probe metadata (RDP) ─┐
        ├──► restriction-rule events ──────┤──► syslog-ng ──► SIEM
        └──► session lifecycle events ─────┘
                         │
                         ▼
            AUDITOR replay (embedded player)  /  Access Manager cross-Bastion search
```

### The Session Probe (RDP / Windows only)

> Glossary: "Mode only available on RDP Windows target servers allowing the collection of a rich set of session metadata … It creates **passive monitoring** … and interrupts neither sessions nor user actions." **Enabled by default** on the RDP connection policy.

It runs *inside the user's RDP session at the user's privilege level* (so **no extra attack surface**, no install) and reports metadata such as:

- change of active window; button presses; radio/checkbox selection; text-field changes; keyboard-layout change;
- process start/stop; clipboard file exchange; redirected-drive file exchange.

It can also **block TCP jump connections** (a session that hops through a target to reach a third host), and — crucially — **protects passwords**: when the input cursor enters a password field or a **UAC (User Account Control)** window appears, the Probe tells the Bastion to **pause keyboard-input capture**. If the Probe stops, the Bastion stops the session. A *catch-up* fallback (retry without Probe) exists for setup only, **not production**.

### Restriction rules — `kill` / `notify` and OCR

> §12.7: "A restriction is a rule that triggers a specific action when certain **character sequences are detected in data sent from the client to the server**." Applied to **user groups and target groups** (the union of patterns; **most restrictive action wins** — if any group says `kill`, it's `kill`).

Two actions: **`kill`** (disconnect) and **`notify`** (email). Rules are **regular expressions**, one per line, **case-sensitive**.

- **SSH:** matched on the upward command-line input.
- **RDP:** matched on keyboard input **and window title bars** via prefixes:

| Prefix | Detection context |
|---|---|
| `$kbd:` | Keyboard input |
| `$ocr:` (or no prefix) | **Title bar of the active window (OCR)** |
| `$kbd-ocr:` / `$ocr-kbd:` | Both |

Match-behaviour prefixes: `$content:` (substring), `$exact-content:`, `$regex:` (default), `$exact-regex:`. Examples from the guide:

```
$ocr:Command Prompt          # block the command prompt window from opening
$ocr:.*\\cmd.exe
$content,ocr:abc.exe         # any active window title containing abc.exe
$kbd:del\s+.*                # keyboard "del ..." command
```

> When a `kill` fires on an active window title, the user is disconnected and **cannot reconnect until the window closes or its title changes**. For SSH you can set a **warning count** (`Configuration > SSH proxy`) to warn N times before disconnecting. SCP/Cisco-style allow-lists are likewise supported.

---

## 5. Real-time monitoring, session sharing, and Session Invite

Glossary definitions are unambiguous:

| Mechanism | Definition |
|---|---|
| **4 eyes** | "Mechanism allowing an **auditor to monitor** the session of another user **without gaining control** over it." |
| **4 hands** | "Mechanism allowing an auditor to **gain control** over the current session of another user." |
| **Session sharing** | "Real-time audit capability which grants auditors access to a user's session … Auditors of RDP sessions can **remotely control** a user's session." |

```
   4 EYES                              4 HANDS
 +----------+   watch only          +----------+   takes control
 |  USER    |                       |  USER    |
 +----+-----+                       +----+-----+
      | session                          | session (shared control)
      v                                  v
 +----------+                       +----------+
 | AUDITOR  | (view, can terminate) | AUDITOR  | (mouse+keyboard, RDP)
 +----------+                       +----------+
```

### Session Invite (external guest)

> §12.8: a **host** (privileged user) shares their **live RDP or VNC** session with an external **guest** who has **no account** in Bastion or Access Manager.

- Granted via the **Session invite** option on the authorization; modes **View only** or **View and control**.
- **Only through Access Manager 5+**; **not** for SSH or applications; **not on WALLIX One PAM SaaS**.
- The guest joins via an **expiring invitation link** — no authentication, the link is sufficient. Default link timeout **600 seconds** (`Session Invite request timeout`).
- The guest's session is **bound to the host's**: when the host disconnects/times out, the guest is dropped; **no separate timeout** for the guest.
- When recording is on, **both** host and guest sessions are recorded; logs carry `[control_owner]` (HOST/GUEST) and `[mode]` (view-only/view-control), all under the host's session ID. The administrator who enabled invite and the host bear responsibility for guest actions.

---

## 6. Approval workflows

> §13.3: "The approval workflow is a mechanism to manage access to sessions and secrets. When a user wants to access sessions or secrets … they must submit a request to the approvers first."

**Two preconditions to *be* an approver:** (1) **Modify** on the *Manage Approvals* feature in the permission profile of every member of the approver group; (2) the group is listed in the **Approvers** section of the authorization's Approval tab.

**Quorum** = the minimum number of favourable answers required. A request is **accepted** when the quorum is reached, **rejected** the moment one approver rejects, **pending** until then, and **closed** when its duration expires (or the user/target/authorization is deleted, or the accepted request times out before connection).

The Approval tab configures **two independent rule sets** — one **inside** the authorized time frame, one **outside**:

| Setting | Inside time frame | Outside time frame |
|---|---|---|
| Options | No approval required / Automatic approval (notify) / **Approval with quorum (N)** | **Access blocked** / Automatic approval / Approval with quorum (N) |

Plus:

- **Comment** — *Mandatory* forces user **and** approvers to give a reason.
- **Ticket** — *Mandatory* forces a ticket reference (external ticketing integration via the approval-workflow script).
- **Approval timeout** — if the user never connects, the accepted request auto-closes; sets the max value approvers may reduce.
- **Single connection** — the approval authorizes the session **only once** (does *not* apply to secret checkout).
- **Self-approval** — globally toggled by `Allow self approvals`; if cleared, approvers can't see/answer their own requests.
- Quorum **N must be ≤ number of approvers** available in the selected groups. Approvers can **reduce** a request's duration (decreases cumulatively).

```
  USER requests access (web or at SSH/RDP connect)
        |
        v
  Approval workflow enabled?
   no -> direct access
   yes ->  inside time frame ?
            | yes                                 | no
            v                                      v
   No approval / Automatic /              Access blocked / Automatic /
   Approval with quorum                   Approval with quorum
            |                                      |
            +------------------+-------------------+
                               v
                quorum reached? --no--> pending ... -> rejected / timeout -> CLOSED
                               | yes
                               v
                ACCEPTED -> session may start (Single connection? then one shot)
                (comment/ticket recorded; SIEM logged)
```

> **Gotcha (verbatim intent):** with *Access blocked* outside hours, an approval that **starts inside** the allowed window can **continue into blocked hours** — only the start time is checked; the session ends when the **approval** ends, not when the time frame ends. Also: **scenario accounts cannot be used with authorizations that include an approval workflow** (use a separate authorization without approval).

---

## Acronyms

| Acronym | Expansion |
|---|---|
| SSH / SCP / SFTP | Secure Shell / Secure Copy / SSH File Transfer Protocol |
| RDP / RDS | Remote Desktop Protocol / Remote Desktop Services |
| VNC | Virtual Network Computing |
| UT / RAW TCP/IP | Universal Tunneling |
| WEBAPP / RBI | Web application proxy / Remote Browser Isolation |
| OCR | Optical Character Recognition |
| UAC | User Account Control (Windows) |
| MFA | Multi-Factor Authentication |
| SIEM | Security Information and Event Management |
| CCN-STIC | Spanish CCN security guidelines |
| SOG-IS CES | SOG-IS Crypto Evaluation Scheme |
| X11 | X Window System protocol |
| WAM | WALLIX Access Manager |

Full list: [../reference/acronyms.md](../reference/acronyms.md).

---

## Sources

- WALLIX Bastion **12.3.2** *Functional Administration Guide*: §5.1 (supported protocols), §11.4 (Connection policies + built-in policies + back-leg auth methods), §12.7 (Restriction rules; RDP/SSH detection patterns, OCR prefixes), §12.8 (Session invite), §12.16.1.4 (Session Probe mode), §13.2 (Authorization parameters — SSH/RDP sub-protocols, CVE-2020-15778 note), §13.3 (Approval workflow), §18.1 (Glossary — 4 eyes, 4 hands, Session, Session probe, Session recording, Session sharing, Session invite). https://pam.wallix.one/documentation/admin-doc/bastion_en_administration_guide.pdf
- CVE-2020-15778 (SCP command injection). https://nvd.nist.gov/vuln/detail/CVE-2020-15778
- Cross-reference: [../docs/00-overview/product-portfolio.md](../docs/00-overview/product-portfolio.md#session-management).

> **Flagged uncertainties:** the detailed live-monitoring/replay UI (the auditor experience for 4-eyes/4-hands) is documented chiefly in the *Sessions Audit Guide* / *Users and Approvers Guide* rather than the Administration Guide — *not specified in detail* in the administration sources cited here. The exact OCR engine internals are not published.
