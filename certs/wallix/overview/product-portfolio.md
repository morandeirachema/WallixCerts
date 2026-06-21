# WALLIX Product Portfolio — Technical Overview for Certification Study

*Compiled 2026-06-17 from WALLIX primary documentation (datasheets, admin/deployment guides, press releases) and reputable secondary sources. Version-specific facts and uncertainties are flagged inline. A full Sources list is at the end.*

---

## Company Background

**WALLIX** is a European (French) cybersecurity software vendor specializing in **identity and access security**, best known for **Privileged Access Management (PAM)**, and extending into identity governance, identity-as-a-service, endpoint privilege management, and industrial (OT) security.

- **Founded:** 2003, Paris, France. Founder and long-serving CEO: **Jean-Noël de Galzain**.
- **Headquarters:** Paris, France.
- **Public listing:** Euronext Growth Paris, ticker **ALLIX** (ISIN FR0010131409); IPO in 2015 — per WALLIX, the first French cybersecurity software company to list on the stock exchange.
- **Scale (per WALLIX's June 2025 "10 years of listing" communication):** revenue grew from ~€4M (2014) to ~€34M (2024); 3,500+ customers across ~90 countries; ~248 staff in 16 countries; recurring revenue ~68% of billings. WALLIX positions itself as the **European leader in PAM**.

### Key acquisitions (confirmed)

| Year | Company | Brought to WALLIX |
|---|---|---|
| 2019 | **Trustelem** (French) | IDaaS / SSO / MFA → WALLIX Trustelem (WALLIX IDaaS) |
| 2019 | **Simarks** (Spanish) | EPM technology → launched as **BestSafe** (Feb 2020) |
| 2023 | **Kleverware** (French) | Identity & Access Governance → **WALLIX IAG** |
| 2025 | **Malizen** (French) | AI-driven user-behavior analytics (anomaly detection from 2026) |

> **Important correction (flag for study):** Sources do **not** support a WALLIX *acquisition* of **inWebo**. inWebo is a long-standing **technology partner/alliance**, not a subsidiary. The **WALLIX Authenticator** MFA app is *powered by / OEM'd from* inWebo's (ANSSI/CSPN-certified) MFA technology. Separately, inWebo itself merged with Belgium's TrustBuilder and rebranded the group to **TrustBuilder** — an entity independent of WALLIX. Likewise, "**BestSafe**" is a WALLIX *product* built on the **Simarks** acquisition — not its own acquired company.

### Market positioning & company-level certifications

- **Gartner Magic Quadrant for PAM:** Leader in 2022, then **Visionary** in 2023, 2024, and 2025 (three consecutive years). Consistently cited as the **only European vendor** in the PAM Magic Quadrant.
- **KuppingerCole Leadership Compass for PAM:** **Overall Leader** for five consecutive years through the 2026 edition.
- **European sovereignty** is a core positioning theme.
- **ISO/IEC 27001:2022** company certification.
- **ANSSI CSPN** (France's first-level security certification) on WALLIX Bastion (see Bastion section).
- **BSI BSZ** (Germany's accelerated security certification), recognized by ANSSI via Franco-German mutual recognition (~late 2025).
- **Common Criteria / EAL:** *no specific EAL level confirmed* — flag as uncertain rather than assert.

---

## 1. WALLIX Bastion — Privileged Access Management (PAM)

### What it is and the problem it solves

WALLIX Bastion is WALLIX's flagship **Privileged Access Management** product. It provides **centralized control, brokering, and monitoring of privileged access** to sensitive IT/OT assets. Stolen/abused privileged credentials are a leading breach vector; Bastion sits as a **trusted gateway/proxy** between a low-trust domain and a high-trust domain so that administrators never need to know target passwords, all sessions are recorded and auditable, and privileged credentials are vaulted and rotated.

It is **agentless** on targets, and deployable **on-premises, in private/public cloud, as SaaS, and hybrid**.

WALLIX frames Bastion around four pillars: **Reduce the attack surface** (asset discovery, removal of local privileged accounts, least privilege, Just-in-Time access), **Control sessions** (real-time monitoring, recording, alerting/termination), **Manage secrets** (vaulting, automated rotation, removing passwords from disks/scripts), and **Audit activity** (KPIs/dashboards, SIEM correlation).

### Main modules

- **Session Manager** (license-gated `Sessions` authorizations): Brokers and authenticates privileged connections; grants only authorized users access to authorized targets; records sessions as full-color video + transcript/keystroke metadata; real-time monitoring; session sharing (4-eyes/4-hands); alerting and forced termination. Target credentials are never exposed to the user.
- **Password Manager / Vault** (license-gated `Secrets` authorizations): Encrypted secrets vault for passwords and SSH keys of human and non-human accounts; password complexity policy; automated rotation; check-out/check-in; password change/verification via plugins; external-vault integration.
- **Access Manager (WAM):** A separate front-end component — an **HTML5 web access gateway / reverse proxy** in front of one or more Bastions, providing a single secured HTTPS entry point for remote/external access (detailed below).

The broader portfolio also includes **PEDM** (privilege elevation/delegation, endpoint local-admin removal — see BestSafe) and the **WALLIX One** console; these are distinct from Bastion's core modules.

### Core PAM concepts — the ACL data model

*(Source: WALLIX Bastion Functional Administration Guide; the served document was version 12.3.2.)* The rights engine is built on **Access Control Lists** of these objects:

- **User / User group** — a user is a physical person (local, LDAP/AD/Azure AD, or SAML/OIDC-federated). User groups simplify authorization assignment; time frames/restrictions attach to groups.
- **Device / Service / Application / Resource** — a *device* is physical/virtual equipment (by name, IP/FQDN, or CIDR subnet); a *service* is protocol+port+connection-policy on a device; an *application* runs on a Windows jump server; a **resource** = service + (device or application).
- **Account (target account)** — an entity used to authenticate to a system = {device, service, account}. **An account always belongs to a domain.** Types: global, device/local, application, and scenario accounts (automate su/sudo at SSH session start).
- **Domain (local vs global)** — a **global domain** groups accounts that authenticate across multiple devices (vault type Local = Bastion vault, or External = external-vault plugin); a **local domain** groups accounts for a single device.
- **Target** = a **resource + a target account**.
- **Target group** — gathers systems with similar requirements so they share authorizations.
- **Authorization** — the binding object that **gives a user group access rights to a target group**. Critical rule: **one authorization links exactly one user group to one target group** (no duplicate pairs). It carries two cumulative rights — **Sessions** (open sessions) and **Secrets** (retrieve/view credentials) — plus allowed protocols/sub-protocols, session-recording toggle, session-invite mode, a Critical-targets flag, and an Approval-workflow tab.

**Relationship chain:** *users → user groups → (authorization) → target groups → targets (resource + account)*.

**User mapping / secondary-connection modes** (how the user actually reaches the target on the Bastion→target leg):
- **Account mapping (user mapping):** user connects with **their own Bastion/directory credentials**, injected automatically (requires `PASSWORD_MAPPING`, or a vault transformation rule for non-password methods).
- **Specific/session account:** connects with a **vault-stored account**, credentials injected automatically.
- **Interactive login:** user **manually types** the target credentials (requires `PASSWORD_INTERACTIVE`; no injection).

**Permission profiles** govern administrative rights (None/View/Modify per feature) and are assignable to users, groups, or API keys.

### Session management

- **Protocols / proxies:** **SSH** (with SFTP/sub-systems), **TELNET**, **RLOGIN**, **RDP**, **VNC**, **RAW TCP/IP** (branded **Universal Tunneling / UT**), **WEBAPP** (web apps), and **standard applications / RemoteApp** via a Windows jump server. The RDP proxy engine is WALLIX's open-source **"Redemption."** RDP supports NLA (default on), Kerberos (default on from 12.0.1), and TLS controls.
- **Sub-protocols** give granular, authorization-gated control (e.g., SSH: shell, remote command, X11, SCP up/down, SFTP, direct-TCPIP; RDP: clipboard up/down, file clipboard, printer, drive, smartcard, audio).
- **Session recording:** Per-authorization. Recordings are **encrypted so only the originating Bastion can replay them**, viewed in an embedded player. RDP/SSH captured as video; textual SSH as transcript. Auditors can also watch current SSH sessions live even when recording is off.
- **Metadata / keystroke / OCR:** The **Session Probe** (RDP Windows targets) passively collects rich metadata (window changes, control operations, process start/stop, clipboard, redirected-drive file exchanges) and pauses keystroke capture on password fields. **OCR-based** restriction rules can `kill` (disconnect) or `notify` on matching window titles / keyboard input; file-size limits gate transfers; Cisco IOS command allow/deny lists are supported.
- **Real-time monitoring / session sharing:** **4-eyes** = auditor monitors without control; **4-hands** = auditor takes control (RDP remote control supported).
- **Session invite (external guest):** Host can invite an external guest into a live **RDP or VNC** session via an expiring link in **Access Manager 5+** (View-only or View-and-control). Not for SSH/applications; not on the SaaS edition; both sessions are recorded.
- **Approval / four-eyes workflows:** Per-authorization Approval tab. Inside the allowed time frame: No approval / Automatic (notify) / **Approval with quorum** (N approvers); outside: blocked / automatic / quorum. Options include mandatory comment, mandatory ticket, approval timeout, single (one-time) connection, self-approval toggle, and external ticketing integration.

### Password / secrets management

- **Secret rotation:** Manual or automatic change of passwords, SSH keys, or both; cron-syntax scheduling; tunable parallelism.
- **Password-change policies:** Default policy requires **min 16 characters** (≥1 special/number/upper/lower) and **RSA key size 4096** (default raised from 8→16 chars in 12.0.6). Supports RSA/DSA/ECDSA key generation.
- **Check-out / check-in:** Checkout retrieves/displays credentials (login, password, SSH key, signed cert) with optional **account lock** preventing concurrent use; checkout policy controls lock, duration/extension/maximum, and **change password at check-in** (forced rotation on return).
- **Password change / verification / propagation:** Manual or automatic; a reconciliation/administrator account is used when Bastion's stored secret diverges from the target.
- **Vault & Break-Glass:** Local Bastion or external vault; emergency credential recovery; nightly GPG-encrypted credential export.
- **Password-change plugins (~20 bundled):** Cisco IOS/Nexus, Citrix ADC, Dell iDRAC, F5 BIG-IP, FortiGate, HP iLO, IBM AIX/3270, Juniper SRX, LDAP, MySQL, Oracle, PAN-OS, Unix, Windows/WindowsService, VMware ESX, Check Point Gaia, etc.
- **External vault plugins:** **CyberArk** Enterprise Password Vault, **HashiCorp Vault** (KV v1), **Thycotic Secret Server**, and a remote **Bastion Vault**. External-vault accounts are mapped via global domains.
- **AAPM (Application-to-Application Password Management):** Marketed to eliminate hard-coded passwords in scripts/config files for DevOps/RPA. **Flag:** "AAPM" is a marketing term; technically it is realized via the **Bastion REST API + vault plugins** (the term does not appear by name in the 12.3.2 admin guide chapters reviewed).

### Access Manager (web portal / single point of access / gateway)

*(Source: WALLIX Access Manager Administration Guide; the served document was version 5.2.4.0.)*

- **Role:** Provides connection services between web browsers and targets via **HTML5 clients — no browser plug-in required**. Brokers **RDP/SSH/UT** sessions over **HTTPS in the browser** (no VPN, no fat client). Also lets users display/copy target passwords in the browser.
- **Gateway / reverse proxy:** Sits in front of **one or more Bastions**, reducing the external attack surface to a single secured HTTPS entry point. Authorizations stay in the Bastion — "the user's authorizations are gathered from the bastions of the organization at each login." Each Bastion registers by name + host + REST API key.
- **Multi-tenancy:** "Organizations" each own users + Bastion instances.
- **Authentication / MFA:** Authentication domains of type local, **LDAP/AD**, **SAML 2.0** (WAM as Service Provider; IdP- and SP-initiated; ADFS/Shibboleth), **OIDC** (Authorization Code Flow), **BASTION**, **RADIUS**, and **X.509** certificate (with CRL/OCSP). True MFA via a per-domain factor/priority model. Federated IdPs include **WALLIX Trustelem**. *Flag: FIDO2/OTP/push are not native to WAM — they arrive via the federated IdP over SAML/OIDC.*
- **Centralized audit:** Cross-Bastion search and replay of recordings (Elasticsearch-backed), live session viewing, video download.
- **Deployment:** Virtual appliance for AWS, Azure, GCP, Alibaba, KVM, Hyper-V, Nutanix AHV, OpenStack, VMware vSphere; runs in Docker. HA via multiple WAM instances behind a load balancer; can also load-balance a cluster of Bastions (routing to the Bastion with fewest in-progress sessions).

### Architecture, deployment, HA, integrations

*(Source: WALLIX Bastion 12.0.2 Deployment Guide.)*

- **Appliance types:** Physical (redundant PSUs) and virtual; virtual images for cloud (AWS AMI, Azure Marketplace, GCP, Alibaba, Outscale) and on-prem hypervisors (KVM, Hyper-V, Nutanix AHV, OpenStack, VMware vSphere ≥ ESXi 5.5); plus a generic GPG-signed ISO. OS base is Debian Linux (strongly implied; exact version not printed).
- **Internal components/services:** **MariaDB** database (ports 3306/3307); `redemption` (RDP proxy); `wabgui` (admin GUI); `wabrestapi` (REST API); `sashimi`; `wallixsession`; `wallixcelery`; `wallix-discovery`; `superset` (analytics/dashboards); `syslog-ng` (SIEM forwarding); `wab-backupdaemon`; `wabwatchdog`. Storage on LVM (`/var/wab`).
- **High Availability:** **In v12, DRBD file-system replication was removed**; HA is now **HA Database Replication** over an autossh SSH tunnel (port 2242; replication 3307→3306). Two modes: **Master/Slave(s)** and **Master/Master** (exactly two nodes), managed by the `bastion-replication` CLI. Key limits: **audit/session tables are NOT replicated** (each node keeps its own), **IPv4 only** in HA, all nodes must run the same version. **Clustering** and disaster recovery are also offered.
- **Scalability:** No fixed concurrent-session/sizing numbers published in the deployment guide (deferred to the support portal). Vertical scaling via CPU/RAM and LVM disk extension for recording retention.
- **Directory / authentication integration:** AD & LDAP (with AD Silos / Protected Users), Kerberos, RADIUS, TACACS+. SAML IdPs include Microsoft Entra ID (Azure AD), Okta, PingIdentity, Google, AWS IAM Identity Center, inWebo, Trustelem.
- **MFA:** External via RADIUS/SAML; WALLIX Trustelem; smart cards (e.g., Gemalto SafeNet IDPrime MD, YubiKey 5 NFC).
- **SIEM / monitoring:** Syslog (`syslog-ng`, port 514), SNMP (v2c/v3), email notifications, Superset dashboards.
- **Encryption:** AES-256, SHA-2, ECC; **encryption at rest = LUKS** (dm-crypt); RSA private keys ≥ 3072 bits; cryptographic policy selectable via `WABSecurityLevel`, with **SOG-IS CES 1.3 (valid to 2030)** recommended.

### Product certifications / standards

- **ANSSI CSPN:** WALLIX Bastion **version 6.0.102** awarded CSPN, announced **9 January 2020** (a renewal). WALLIX describes Bastion as the first market solution awarded CSPN by ANSSI. (Carried forward in positioning through later versions.)
- **BSI BSZ (Germany):** Obtained; reinforces European public-sector positioning.
- **Common Criteria / EAL:** **No EAL certification found** in sources consulted — flagged as a likely absence; the official ANSSI/CC catalogues would be the definitive check.
- **Regulatory positioning (not product certifications):** NIS2, GDPR, IEC 62443, DORA.

---

## 2. WALLIX One — the Cybersecurity SaaS Platform

### What it is (and disambiguation)

**WALLIX One is WALLIX's cybersecurity SaaS platform** — a "Security-as-a-Service" brand/umbrella under which WALLIX delivers its access- and identity-security products as cloud-hosted subscription services. It is **not a single product**; it is the platform/delivery model through which several WALLIX services are consumed.

- WALLIX's self-description: "the cybersecurity SaaS platform designed to meet the digital and economic challenges of companies aiming to safeguard their access and identities," offering "best-of-breed Access and PAM services."
- **Launched 14 December 2023.**

**Layering to keep straight (important for the exam):**
- *WALLIX One* = the SaaS platform / delivery model.
- Individual services follow a *"WALLIX One-X"* naming convention (e.g., WALLIX One-PAM, WALLIX One-IDaaS, WALLIX One-RA, WALLIX One Enterprise Vault).
- Underlying technology products (Bastion, Access Manager, Trustelem, BestSafe) are the *engines*; WALLIX One is how some of them are packaged and delivered as SaaS.

### Core problem & target audience

Reduce identity-related breach risk and enable Zero-Trust access governance **without** on-prem infrastructure, CapEx, setup, and maintenance burden — addressing the cybersecurity skills shortage with fast ROI ("WALLIX takes care of it for you"). Targets companies of all sizes, with emphasis on **SMEs/mid-caps/SMBs**, cloud-first organizations, and governance of access for employees, external/third-party providers, IT admins, and OT maintainers. Secondary (blog-level) positioning targets **MSPs** as a cloud-PAM channel play.

### Services delivered under WALLIX One

| Service | What it delivers |
|---|---|
| **WALLIX One-PAM** | PAM as a service — privileged account/password management, session traceability, JIT access. |
| **WALLIX One-IDaaS** | Cloud SSO + MFA, federated identity (built on **Trustelem** technology). |
| **WALLIX One-RA (Remote Access)** | Controlled third-party access with traceability, MFA, auto-revocation; **no VPN, no shared passwords**. |
| **WALLIX One Enterprise Vault** | SaaS credential manager with **end-to-end / zero-knowledge encryption**; encrypted sharing; browser extension + mobile app; admin recovery. |

PAM tiers on the SaaS portal: **WALLIX One PAM Core** (internal users — Session Manager, Password Manager, Universal Tunneling) and **WALLIX One PAM** (adds **Access Manager** for remote/external privileged access). **WALLIX One Console** is the centralized management console for large/distributed environments.

### Architecture / delivery model

- **Pure SaaS**, annual subscription, consumption-flexible, automatic updates, **99.9% uptime SLA**, **ISO/IEC 27001** certified.
- **Agentless / no on-prem connectors:** "WALLIX One PAM does not require the installation of any on-premises connectors." Connectivity is via an **IPSec tunnel initiated outbound from the client network** to the WALLIX One PAM gateway — "no inbound connections or open ports are required on the client's side."
- Protocol proxies: **RDP, SSH/SFTP, VNC, TELNET/RLOGIN**, plus OT protocols and LDAP/Kerberos integration.
- **Relationship to Bastion:** WALLIX One PAM is **Bastion + Access Manager delivered as managed SaaS** — the architecture docs reference deployed components named "WALLIX Bastion - GUI / RDP Proxy / SSH Proxy" alongside WALLIX Access Manager. Bastion is *also* still sold standalone (on-prem and via AWS Marketplace BYOL).

> **Flags / uncertainties:** Single-tenant architecture + Microsoft Azure hosting are reported by secondary sources but were **not directly confirmed** on the wallix.com pages reviewed. The explicit "Trustelem → WALLIX One-IDaaS" rename is strongly implied but not stated verbatim on the pages read. **EPM/BestSafe and PAM4OT belong to the broader WALLIX suite but were not presented as WALLIX One SaaS services** — do not conflate the overall product suite with the WALLIX One SaaS platform.

---

## 3. WALLIX Trustelem — IDaaS (SSO / MFA / Identity Federation)

### What it is and the problem it solves

**WALLIX Trustelem** is WALLIX's **European Identity-as-a-Service (IDaaS)** platform delivering cloud **Single Sign-On (SSO), Multi-Factor Authentication (MFA), and identity federation**, positioned as the IDaaS pillar of **WALLIX One** (sometimes branded "WALLIX One IDaaS"). It unifies and secures workforce access to applications within a **Zero Trust** framework, addressing password vulnerability, application proliferation, and the IT burden of manual access management.

### Key features

- **Single Sign-On:** Authenticate once; SAML/OIDC apps trust the session.
- **MFA factors (confirmed in WALLIX docs):**
  - **WALLIX Authenticator** — mobile (iOS/Android) and desktop (Windows) app; **push** when online, **TOTP** fallback offline. (The MFA tech is *powered by inWebo* — see Company Background.)
  - **TOTP** (also works with Google/Microsoft Authenticator).
  - **FIDO security keys** — FIDO2 hardware keys (e.g., YubiKey) via **WebAuthn** (not usable over LDAP/RADIUS).
  - **SMS OTP** (disabled by default; extra cost) and **Email OTP** (disabled by default; "not strong authentication").
  - Docs stress true strong auth = two different kinds of factors.
- **Authentication methods (datasheet-level, secondary-confirmed):** Password (AD/LDAP/Trustelem-stored), Integrated Windows Authentication, X.509 certificate.
- **Adaptive / contextual access (Access Rules):** Per-application enforcement of no-auth / 1-factor / 2-factor / deny, differentiated by **internal vs. external IP zone**, applied to users/groups/everyone, with most-restrictive-wins and user-over-group priority. *Flag: "adaptive" here is primarily **network/IP-context** based; geolocation/device-posture/time-of-day conditions were not found in the docs.*
- **Self-Service Password Reset (SSPR):** For Trustelem-local, Active Directory (via ADConnect), and Azure AD (non-federated). Admin-configurable verification factors.
- **User lifecycle / provisioning:** Inbound directory sync; outbound provisioning via **SCIM 2.0**; delegated administration; auditing with on-premise SIEM export.

### Supported protocols / standards

- **Federation / SSO:** **SAML 2.0**, **OpenID Connect**, **OAuth 2.0**.
- **Non-federated app auth (MFA but no SSO):** **LDAP/LDAPS** and **RADIUS** (UDP 1812; PAP; typically "2nd factor only").
- **SCIM 2.0:** Trustelem acts as a **SCIM client** to provision users/groups into downstream apps (create/update on grant, deactivate on revoke; ~5-min push interval; relayed via Trustelem Connect).

### Identity sources / directory integration

- **Active Directory** via **Trustelem ADConnect** — an on-prem connector with an **outbound WebSocket to admin.trustelem.com on port 443** (TLS + extra encryption), talking to AD over LDAP(S) with a read-only service account. Syncs users/groups by `memberOf`; **no AD passwords are stored**. Login maps to sAMAccountName, userPrincipalName, or mail.
- **Azure AD / Entra ID** via Microsoft Graph API. *Limitation: when Azure delegates auth to an external IdP or uses federated domains, Azure password auth is unavailable.*
- **LDAP** directories; **Google Workspace** (datasheet/secondary); **Trustelem local users**.

### Architecture / delivery

- **SaaS / cloud-hosted**, **hosted in European data centers** ("European privacy standards"; secondary sources stress European sovereignty / GDPR).
- **On-prem connectors (lightweight agents):** **Trustelem ADConnect** (AD sync + auth delegation) and **Trustelem Connect** (local LDAP/RADIUS server + SCIM forwarder; outbound 443 WebSocket — no inbound firewall opening).
- Per-customer tenant domain `https://<tenant>.trustelem.com`; web admin console.

### Integration with Bastion / WALLIX One

- Pre-integrated for **WALLIX Access Manager** (via **SAML 2.0** recommended, or RADIUS) and **WALLIX Bastion** (via **LDAP/RADIUS**), providing MFA/SSO to PAM.
- Bundled into **WALLIX One** (Dec 2023) alongside PAM and Remote Access, managed from the WALLIX One Console; MFA is natively integrated with WALLIX PAM.

### Application catalog

- A catalog of **pre-integrated app connectors**. *Flag: count is uncertain/conflicting — docs suggested "80+", a third party claimed "1000+"; wallix.com did not state a count on the pages reviewed.* Named apps include Microsoft 365, Google Workspace, Salesforce, Dropbox, AWS, GitHub, Slack, Box, Datadog, Zendesk, Tableau, plus WALLIX Bastion and Access Manager. Generic models exist for SAML 2.0, OIDC, OAuth 2.0, and "Basic / no SSO" (LDAP/RADIUS) apps.

---

## 4. WALLIX BestSafe — Endpoint Privilege Management (EPM)

### What it is and the problem it solves

**WALLIX BestSafe** is WALLIX's **Endpoint Privilege Management (EPM)** product — "a modular endpoint protection solution based on simple rules" designed to "eliminate the risks associated with overprivileged users and avoid the spread of malware, crypto-viruses and ransomware attacks." Because privilege escalation underpins most attacks, BestSafe operationalizes **least privilege** on endpoints, letting an organization remove local administrator accounts and "create a zero-administrator policy" while users stay productive (they can still run the apps they need, even privileged ones). It targets both user workstations and application servers, and is built on technology from the **Simarks** acquisition.

### Distinguishing technical approach — privilege at the PROCESS/APPLICATION level

This is the central differentiator (verbatim from the datasheet): *"BestSafe uses WALLIX's exclusive **patented technology** to assign the necessary security context to each process or application, regardless of the user credentials with which it is executed. With BestSafe, privileges are granted to **applications instead of users**, unlike traditional tools on the market."*

- Traditional models elevate the *whole user* (local admin membership, UAC, sudo, "run as administrator") — so any malware in that user's context inherits the rights.
- BestSafe instead attaches the required privilege to the **specific process/application + context**, leaving the user a standard non-admin account, making **"the operating system itself the guarantor of security."** The user cannot self-elevate; local admin can be removed entirely; sanctioned apps still get exactly the privileges they require; and **"the most dangerous API calls are blocked"** even within otherwise-allowed apps. WALLIX positions this as **PEDM** (Privilege Elevation and Delegation Management).

### Key features

| Feature | Detail |
|---|---|
| **Application control** | White / gray / black listing; blocks unwanted installs; lets users self-install an approved set without IT. |
| **Privilege management** | At the application level and the user level; granular per user/application/group. |
| **Anti-ransomware** | **Detect in real time when a process intends to perform an encryption operation *before it is carried out***, then stop it; optionally store every encryption key to allow later decryption. |
| **Local Account Password Rotation** | Rotates each local-account password to be **unique per computer, per account, per day**; future passwords predictable offline (no network needed); change attempts alerted. |
| **Local user management** | Rule-based group membership + password rotation. |
| **Monitoring & analytics** | Event-based; **SIEM integration**; alerts/alarms. |

> *Flag on "credential theft protection":* BestSafe addresses credential abuse mainly via (a) eliminating local admin accounts and (b) per-machine/per-day local password rotation. A discrete "credential theft protection" module beyond this is **not named in the datasheets** — treat broader credential-theft wording as positioning, not a distinct documented feature.

### Architecture

- **Agent-based:** a **light agent** per endpoint that caches its configuration locally and **enforces policy even offline**.
- **Active Directory-native, no extra infrastructure:** "Fully integrated into Microsoft Active Directory"; "does not require additional infrastructure (DB servers, web servers, etc.)"; the agent contacts the closest Domain Controller.
- **Management plane:** **MMC snap-in** + AD integration (policy distributed AD/GPO-style); event-based monitoring with SIEM forwarding. *Flag: whether current BestSafe/EPM is managed via the WALLIX One Console is plausible but not confirmed in the primary BestSafe sources — version-dependent.*
- WALLIX cites a client-server model for scalability ("100% scalable at zero cost") and very fast deployment.

### How it complements PAM (endpoint vs. session side)

WALLIX pairs BestSafe with Bastion as a combined **PAM/PEDM** offering under the **"PAM4ALL"** least-privilege vision:
- **Bastion (PAM) = session side** — brokers, vaults, records, and audits privileged sessions/credentials to targets.
- **BestSafe (EPM/PEDM) = endpoint side** — enforces least privilege on the workstation/server itself, at the process/application level, removing standing local admin rights.

### Platforms supported

From the 2021 datasheet (authoritative): **Windows XP and Server 2003**, **Windows Vista and above** (covers modern Windows 10/11 and current Server editions), and **Linux (Debian, RedHat, SUSE)** with fine-grained policy-based elevation on Unix/Linux. *Flag: **macOS is NOT listed** in the WALLIX BestSafe datasheets; some third-party summaries assert macOS support, but it is **unconfirmed / likely not supported** for BestSafe specifically.*

---

## 5. WALLIX IAG — Identity & Access Governance

### Disambiguation (read first)

The naming confusion resolves into two **separate** WALLIX moves:

- **WALLIX IAG (Identity & Access Governance) = the Kleverware product.** WALLIX acquired **Kleverware** (a French IAG vendor) on **16 May 2023** and rebranded "Kleverware IAG" as **WALLIX IAG**. Confirmed verbatim on the WALLIX IAG datasheet: *"The addition of the WALLIX IAG solution seamlessly complemented their existing portfolio following the acquisition of Kleverware."* **IAG is an official WALLIX product name — confirmed, not ambiguous.**
- **inWebo has nothing to do with IAG.** inWebo is a strong-authentication/MFA vendor; WALLIX's relationship is a **technology partnership** powering **WALLIX Authenticator** (the MFA app tied to Trustelem). **WALLIX did not acquire inWebo** (inWebo merged with TrustBuilder separately). Do not conflate inWebo with IAG.

So: **IAG ← Kleverware (acquisition). MFA/Authenticator ← inWebo (partnership).**

### What it is and the problem it solves

WALLIX IAG is the **governance layer** answering *"who has access to what, and should they?"* — "a formal way of managing and governing access entitlements within an organization," providing "a comprehensive mapping of identities to their respective permissions" and acting as a control tower for access-certification campaigns. WALLIX distinguishes IAG (governance overlay) from IAM (the authentication/authorization plumbing); IAG can run standalone or complement an existing IAM.

Core problems solved: who-has-access-to-what visibility, **access certification/recertification**, **Segregation of Duties (SoD)** / toxic-rights detection, orphan/over-entitled account remediation, and compliance reporting (ISO 27001, SOX, Basel III, NIS2, PCI DSS, Solvency II, DORA, GDPR, HIPAA).

### Key features and components (four pillars)

| Pillar | Capabilities |
|---|---|
| **Access Identification / Modelization** | Centralized view across internal IT + cloud apps; data consolidation from directories, cloud, file systems, applications via an **ETL**; exhaustive mapping of privileged accounts; role-based attribution models. |
| **Lifecycle Management (Joiner-Mover-Leaver)** | Validation/consistency of authorizations via business-line managers; continuous control for arrivals, transfers/mobility, departures; recertify at mobility. |
| **Risk Control** | Detect orphan / over-allocated accounts; enforce **SoD** and identify toxic combinations; remediation executed via third-party systems (**WALLIX PAM, ITSM, IAM**). |
| **Audit & Compliance** | Auditability of (privileged) accounts; auditor-tailored reports; **review/recertification campaigns** (configurable duration, periodicity, scope, approvers); remediation workflow; compliance dashboards. |

Web-interface driven; request workflows integrate with the customer's ITSM; automated campaign alerts.

### Fit in the broader portfolio

IAG is the newest pillar (since 2023) alongside Bastion (PAM), Trustelem (IDaaS), and BestSafe (EPM). WALLIX markets the **convergence of IGA + PAM** — pairing IAG with Bastion yields **Privileged Access Governance (PAG)**: governance campaigns and SoD applied to privileged accounts, with PAM as the enforcement/remediation arm. Also pitched for IT/OT and NIS2/DORA compliance.

> **Confidence:** High that IAG = the Kleverware-derived official product (per WALLIX's own datasheet). High that inWebo ↔ Authenticator/MFA and is unrelated to IAG. The €250k Kleverware price and dates come from press-wire snippets consistent across multiple secondary sources but the full primary PR could not be opened directly.

---

## 6. WALLIX PAM4OT — Operational Technology (OT) Security

### What it is and the problem it solves

**PAM4OT** is WALLIX's PAM offering purpose-built for **Operational Technology** environments — ICS, SCADA, PLCs/RTUs, HMIs, engineering workstations. It is delivered under the **OT.security by WALLIX** brand (launched 6 October 2022) and described as "a unified set of state-of-the-art functionalities for securing access and identity in all industrial operations."

**Core problem:** control, secure, and audit *privileged access* to OT/ICS assets — especially **remote third-party/vendor and maintenance access** — without disrupting production. PAM4OT inserts a controlled, monitored broker between users and OT assets, enforcing least privilege, JIT access, and full session traceability.

> **Product vs. packaging (important):** PAM4OT is **not a separately-engineered product**. WALLIX's launch material describes it as a **dedicated package built on WALLIX PAM (the Bastion product line)** — sessions "flow through the WALLIX Bastion." Treat PAM4OT as an **OT-specific packaging/positioning of WALLIX Bastion** (Session Manager, Password Manager/Vault, Access Manager, PEDM, AAPM, Authenticator) plus WALLIX Remote Access.

### How it differs from standard IT PAM

- **Agentless / no software on PLCs or endpoints** — no performance impact on target equipment (the single most-emphasized OT differentiator; PLCs/RTUs/legacy HMIs can't host agents).
- **Legacy industrial protocol support via encapsulation** — industrial protocols (Modbus, PROFINET, S7, EtherCAT, etc.) can be **encapsulated inside an SSH tunnel** for controlled, traceable PLC sessions (in some configs, direct PLC connection without a separate jump server).
- **Production continuity over IT-style policy** — secure any protocol/access without impacting production; HA/24-7 emphasized.
- **IT/OT boundary and segmentation awareness** — operates at the boundary between segmented IT and OT networks.
- **Third-party maintenance access as a first-class use case** — WALLIX cites securing 7,000+ remote access points for OT service providers in 2023.

### Key features

- **Secure remote access for external maintenance providers** — brokered/gateway model; remote vendors authenticate to the WALLIX gateway, not directly to OT assets; integrates with AD/LDAP/RADIUS/SAML.
- **Clientless, browser-based access** — via WALLIX Access Manager / Web Session Manager; no plug-ins.
- **Session recording for OT** — video-style playback, keystroke logging, command capture, **OCR** for graphical sessions; real-time monitoring/intervention.
- **Protocol support** — **RDP, SSH, VNC, Telnet, HTTP/HTTPS** to Windows/Linux systems, network devices, HMIs, engineering workstations, plus industrial-protocol encapsulation in SSH tunnels.
- **Strong authentication (MFA)** via WALLIX Authenticator.
- **Password/credential management** via WALLIX Password Manager with **automatic credential injection** (operators never see passwords).
- **Just-in-Time access & least privilege / PEDM** — time-limited, task-scoped elevation; sessions terminate on completion.

### Architecture / IT-OT boundary positioning

- Operates as a **centralized brokered access point (bastion/jump host)** between users/remote vendors and OT assets; all privileged sessions route through WALLIX Bastion (authentication, credential injection, protocol proxying, recording).
- In the **Purdue Reference Model**, this is the role of a jump/bastion host in the **Level 3.5 Industrial DMZ** between OT (Levels 0–3) and IT/enterprise (Levels 4–5). *Flag: the explicit "Level 3.5" label comes from general OT-architecture sources; WALLIX pages speak of "IT/OT boundary" and segmentation rather than publishing a Level 3.5 diagram.*
- **Deployment:** on-prem, private/public cloud, hybrid, and SaaS (WALLIX Remote Access / WALLIX One). Agentless on the target side.

### Standards / compliance

- **ISA/IEC 62443** — central OT standard; WALLIX publishes a whitepaper mapping Bastion PAM to 62443 essentials. (Detailed zone/conduit/Foundational-Requirement/SL mappings are in the gated whitepaper PDF, not the public page.)
- **NIS2 Directive (EU)** — cited as a driver (traceability/monitoring for audit-readiness).
- **NIST Cybersecurity Framework and NIST SP 800-82** (ICS guidance).
- **NERC CIP** — named in the Schneider i-PAM context and broader OT messaging, alongside the NIS Directive, France's LPM, and ISO 27001.
- European credentials: ANSSI certification and the "Cybersecurity Made in Europe" label.

### Partnerships (OT/ICS vendors)

- **Schneider Electric** — the most substantive OT alliance. Joint **Industrial PAM (i-PAM)** solution; WALLIX provides **"WALLIX Inside,"** an embedded form of its PAM tech that Schneider embeds into its **Harmony P6 "Edge Box"** line. Positioned for NIS, LPM, ISO 27001, NERC CIP, NIST SP 800-82. Schneider is a WALLIX "Elite Partner."
- **Cisco** — partnership strengthened (announced 27 June 2024) integrating PAM4OT with **Cisco Cyber Vision** (OT asset discovery) for centralized monitoring, JIT access, protocol restriction, and traceability.
- **Nozomi Networks** — technology alliance (20 September 2022) integrating PAM4OT with Nozomi's OT/IoT asset discovery and behavioral threat detection toward a Zero-Trust OT architecture.

> **Flags:** PAM4OT = packaging of Bastion/WALLIX PAM for OT (confirmed via WALLIX's launch PR). Some richest feature detail (protocol encapsulation, OCR, direct-PLC connection, agentless no-performance-impact) came from search extracts of WALLIX/reseller pages rather than fully fetched primary HTML — credible and consistent, but verify against a WALLIX datasheet PDF if exact wording is needed.

---

## Sources

### WALLIX Bastion / PAM
- https://www.wallix.com/products/privileged-access-management/
- https://www.wallix.com/wp-content/uploads/2021/10/DATASHEET_2021_BASTION_EN.pdf
- https://pam.wallix.one/documentation/admin-doc/bastion_en_administration_guide.pdf (served version 12.3.2)
- https://marketplace-wallix.s3.amazonaws.com/bastion_12.0.2_en_deployment_guide.pdf
- https://www.wallix.com/wp-content/uploads/2020/07/WALLIX_BASTION_ACCESS_MANAGER_EN.pdf
- https://pam.wallix.one/documentation/admin-doc/am-admin-guide_en.pdf (served version 5.2.4.0)
- https://www.wallix.com/wp-content/uploads/2020/08/20200113-CSPN_EnglishVersion.pdf
- https://www.wallix.com/news/wallix-bastion-honored-again-cspn-certification
- https://www.wallix.com/en/actualites/wallix-bastion-distingue-certification-cspn-anssi
- https://support.wallix.com/hc/en-us/articles/24928252714013-Compatibility-Between-Bastion-and-Access-Manager (referenced in WAM guide)
- https://support.wallix.com/s/article/Wallix-Bastion-sizing (referenced in deployment guide)

### WALLIX One
- https://www.wallix.com/products/wallix-one/
- https://www.wallix.com/press/2023/introducing-wallix-one-the-cybersecurity-saas-platform-designed-to-meet-the-digital-and-economic-challenges-of-companies-aiming-to-safeguard-their-access-and-identities/
- https://pam.wallix.one/
- https://www.wallix.com/products/enterprise-vault/
- https://pam.wallix.one/documentation/deployment/getting-started/architecture.html
- https://www.prnewswire.com/news-releases/introducing-wallix-one-the-cybersecurity-saas-platform-designed-to-meet-the-digital-and-economic-challenges-of-companies-aiming-to-safeguard-their-access-and-identities-302013994.html
- https://www.wallix.com/products/remote-access/
- https://www.wallix.com/blogpost/winning-the-future-of-pam-in-the-cloud-how-wallix-saas-is-redefining-security-for-mses-and-smbs/
- https://incyber.org/en/article/wallix-launches-saas-platform-dedicated-to-access-and-identity/
- https://aws.amazon.com/marketplace/pp/prodview-n5llbkfguwale

### WALLIX Trustelem (IDaaS / MFA / SSO)
- https://www.wallix.com/products/idaas/
- https://www.wallix.com/products/multi-factor-authentication-mfa/
- https://trustelem-doc.wallix.com/books/trustelem-administration/page/summary
- https://trustelem-doc.wallix.com/books/trustelem-administration/page/multi-factors-authentication
- https://trustelem-doc.wallix.com/books/trustelem-administration/page/ldap-radius-trustelem-connect
- https://trustelem-doc.wallix.com/books/trustelem-administration/page/active-directory-users-trustelem-adconnect
- https://trustelem-doc.wallix.com/books/trustelem-administration/page/azure-ad-users
- https://trustelem-doc.wallix.com/books/trustelem-administration/page/access-rules
- https://trustelem-doc.wallix.com/books/trustelem-administration/page/scim-client
- https://trustelem-doc.wallix.com/books/trustelem-administration/page/self-service-password-reset
- https://trustelem-doc.wallix.com/books/trustelem-applications/page/wallix-access-manager
- https://trustelem-doc.wallix.com/books/trustelem-applications/export/html
- https://trustelem-doc.wallix.com/books/wallix-authenticator/page/presentation

### WALLIX BestSafe (EPM)
- https://www.wallix.com/endpoint-privilege-management/
- https://www.wallix.com/blogpost/endpoint-privilege-management-a-new-generation-of-007-2/
- https://www.wallix.com/wp-content/uploads/2020/09/WALLIX_BESTSAFE_2020_EN.pdf
- https://www.wallix.com/wp-content/uploads/2021/10/DATASHEET_2021_BESTSAFE_EN.pdf
- https://www.solutions-numeriques.com/avec-bestsafe-wallix-ajoute-le-endpoint-privilege-management-a-ses-solutions/
- https://idency.com/products/networking/security-management/network-management-security-management/wallix-bestsafe-endpoint-privilege-management-epm/

### WALLIX IAG (Identity & Access Governance) / Kleverware / inWebo
- https://www.wallix.com/products/identity-and-access-governance/
- https://www.wallix.com/blogpost/what-is-identity-and-access-governance-iag/
- https://www.wallix.com/wp-content/uploads/2024/02/DATASHEET_2024_WALLIX_IAG_ENG.pdf
- https://www.wallix.com/alliances/inwebo
- https://www.actusnews.com/en/wallix/pr/2023/05/16/wallix-acquires-kleverware-a-leading-player-in-identity-and-access-governance
- https://kleverware.com/en/wallix-acquires-kleverware-a-leading-player-in-identity-and-access-governance/
- https://www.wallix.com/press/2023/wallix-signs-a-technological-alliance-with-kleverware-to-strengthen-cloud-security/
- https://www.kuppingercole.com/research/bc81430/identity-and-access-governance-wallix
- https://www.wallix.com/blogpost/iga-and-pam-how-identity-governance-administration-connects-with-pam/
- https://docs.trustbuilder.com/mfa/general-overview-getting-started-with-inwebo
- https://inwebo.group/wp-content/uploads/2022/01/PR_inWebo_Technologies_and_Trustbuilder_join_inWebo_Group.pdf

### WALLIX PAM4OT / OT security
- https://www.wallix.com/ot-security/
- https://www.wallix.com/ot-security/ot-products/ot-pam4ot/
- https://www.wallix.com/blogpost/scada-security-and-privileged-access-management-pam/
- https://www.wallix.com/ot/ot-whitepaper/how-wallix-helps-achieve-isa62443-compliance/
- https://www.wallix.com/press/wallix-strengthened-its-partnership-with-cisco-to-cyber-secure-industrial-networks/
- https://www.wallix.com/product-lp/ot-operations-with-remote-access/
- https://www.wallix.com/press/2022/wallix-accelerates-in-the-industry-market-by-launching-ot-security-by-wallix-its-brand-dedicated-to-industrial-cybersecurity/
- https://www.wallix.com/ot-homepage/ot-use-case-secure-remote-access/
- https://www.wallix.com/schneider-electric-i-pam-industrial-privileged-access-management/
- https://www.wallix.com/alliances/schneider-electric

### Company background
- https://www.wallix.com/company/about-wallix/
- https://www.wallix.com/press/wallix-is-ramping-up-its-ai-strategy-with-the-acquisition-of-french-start-up-malizen/
- https://live.euronext.com/en/products/equities/company-news/2025-06-17-wallix-new-european-leader-cybersecurity-celebrates-ten
- https://www.wallix.com/news/wallix-acquires-simarks-workstation-pam-offer-leading-global-player
- https://www.actusnews.com/en/wallix/pr/2020/02/20/wallix-announces-the-launch-of-bestsafe-its-new-endpoint-privilege-management-epm-solution
- https://www.wallix.com/press/wallix-recognized-as-a-visionary-for-the-third-consecutive-year-in-the-2025-gartner-magic-quadrant-for-pam-solutions/
- https://www.wallix.com/press/wallix-recognized-for-the-fifth-consecutive-year-as-an-overall-leader-in-kuppingercole-s-leadership-compass-pam-2026/
- https://www.wallix.com/press/2022/wallix-named-a-leader-in-the-2022-gartner-magic-quadrant-for-privileged-access-management/
- https://www.wallix.com/press/wallix-achieves-dual-certifications-in-germany-and-france-reinforcing-its-position-as-a-trusted-european-cybersecurity/
- https://www.globalsecuritymag.com/WALLIX-has-been-awarded-CSPN,20200113,94520.html
- https://www.trustbuilder.com/en/2-years-of-trustbuilder-after-inwebo/

---

## Key uncertainties flagged (summary)

1. **inWebo was NOT acquired by WALLIX** — it is a technology partner; WALLIX Authenticator (MFA) is *powered by* inWebo. Confirmed acquisitions: **Trustelem (2019), Simarks (2019), Kleverware (2023), Malizen (2025)**.
2. **WALLIX IAG = the Kleverware product** (rebranded), unrelated to inWebo.
3. **PAM4OT is a packaging of WALLIX Bastion/PAM for OT**, not a separate engine.
4. **"BestSafe" is a product** (from the Simarks acquisition), not an acquired company; **macOS support is unconfirmed/likely absent**.
5. **"AAPM"** is a marketing label for Bastion's REST-API + vault-plugin mechanism (not named in the 12.3.2 admin guide).
6. **No Common Criteria EAL** level confirmed for Bastion — only **ANSSI CSPN** (FR) and **BSI BSZ** (DE).
7. **WALLIX One** is the SaaS platform/umbrella; **EPM/BestSafe and PAM4OT were not presented as WALLIX One SaaS services** in the sources reviewed. Single-tenant/Azure hosting is reported by secondary sources only.
8. **Trustelem app-catalog size** (80+ vs 1000+) and a few datasheet-level auth methods are secondary-source only.
9. **Purdue "Level 3.5"** placement for PAM4OT is standard industry framing, not explicit WALLIX page labeling.
