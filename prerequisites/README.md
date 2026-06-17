# Prerequisites — the sysadmin → cyber skill bridge

PAM sits on top of the infrastructure you already know. These pages refresh the systems,
networking, and cryptography fundamentals that WALLIX Bastion brokers and integrates with —
each tied explicitly to *how Bastion uses it*.

| Page | Covers | Tied to Bastion |
|------|--------|-----------------|
| [Linux essentials for PAM](linux-essentials-for-pam.md) | SSH, sudo/su, users/permissions, systemd, logs — and the Linux "PAM" name clash | Debian-based appliance, SSH proxy, WCE-P CLI |
| [Linux CLI deep dive for WCE-P](linux-cli-for-wce-p.md) | Logs, services & ports, REST API via curl/jq, network/crypto helpers, cron & scripting — mapped to WCE-P modules | The Expert-level GNU/Linux CLI prerequisite |
| [Windows & Active Directory](windows-and-active-directory.md) | AD objects, GPO, RDP, NTLM vs Kerberos, privileged groups, LAPS, tiered admin | AD/LDAP integration, RDP proxy, Kerberos auth |
| [Networking & protocols](networking-and-protocols.md) | SSH/RDP/VNC/LDAP/RADIUS/Kerberos/SAML/OIDC/SCIM/Syslog with ports & flows | Every protocol Bastion proxies or authenticates with |
| [Cryptography & PKI](cryptography-and-pki.md) | Symmetric/asymmetric, hashing, TLS, PKI/X.509, SSH keys, TOTP/FIDO2 | AES-256, LUKS at rest, certificate auth, key rotation |

➡️ Next: the [WALLIX product portfolio](../docs/00-overview/product-portfolio.md) and the
[certification tracks](../docs/pam-bastion/README.md).
