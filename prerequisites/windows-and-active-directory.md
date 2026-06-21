# Windows and Active Directory for PAM

Most enterprises run **Microsoft Active Directory (AD)** as their identity backbone, and
most privileged targets are **Windows servers** reached over **Remote Desktop Protocol
(RDP)**. The **WALLIX Bastion** integrates tightly with AD: it authenticates users
against AD/LDAP, brokers RDP sessions through its **"Redemption"** proxy engine, and can
use **Kerberos** to reach targets. To master PAM (Privileged Access Management) you must
first understand the Windows/AD world it protects. This file builds that foundation from
first principles and ties each concept to Bastion.

## Learning objectives

By the end of this file you should be able to:

- Describe **AD objects**: users, groups, **Organizational Units (OUs)**, and
  **Group Policy Objects (GPOs)**.
- Explain the role of a **Domain Controller (DC)**.
- Compare **NTLM** vs **Kerberos** authentication and walk through the Kerberos flow.
- Identify high-value **privileged groups** (Domain Admins, Enterprise Admins) and the
  risk of **service accounts**.
- Explain **LAPS** (Local Administrator Password Solution) and the **Microsoft
  tiered-admin model**.
- Connect AD/LDAP integration, the RDP "Redemption" proxy, and Kerberos auth to how
  WALLIX Bastion operates.

See also [../reference/acronyms.md](../reference/acronyms.md) and
[networking-and-protocols.md](networking-and-protocols.md).

---

## 1. Active Directory objects

**Active Directory (AD)** is Microsoft's directory service: a hierarchical database of
identity and policy objects for a Windows **domain** (e.g., `corp.example.com`). The
core objects:

| Object | What it is | Example |
|--------|------------|---------|
| **User** | A person/account that logs in | `alice@corp.example.com` |
| **Group** | A bundle of users (and groups) for permission assignment | `Domain Admins`, `IT-Helpdesk` |
| **Organizational Unit (OU)** | A container that organizes objects and is the unit GPOs attach to | `OU=Servers,OU=Paris` |
| **Group Policy Object (GPO)** | A policy bundle (security, software, settings) linked to a site/domain/OU | "Disable USB on workstations" |
| **Computer** | A machine joined to the domain | `SRV-DB-01` |

```mermaid
flowchart TD
    D["Domain: corp.example.com"] --> P["OU=Paris"]
    D --> L["OU=London"]
    D --> S["OU=Servers"]
    P --> Pc["Users · Groups<br/>(GPO link)"]
    L --> Lc["Users · Groups<br/>(GPO link)"]
    S --> Sc["Computers<br/>(linked GPOs)"]
```

- **OUs** are about *administration and policy scope* (where a GPO applies).
- **Groups** are about *permissions* (who can access what). Don't confuse them.

> **Bastion tie-in:** Bastion connects to AD over **LDAP/LDAPS** (Lightweight Directory
> Access Protocol, ports **389/636**) to authenticate users and **map AD groups to
> Bastion user groups**. You define an AD group like `PAM-Admins`, and Bastion grants
> those members the matching authorizations — so AD remains the single source of truth.

---

## 2. Domain Controllers (DCs)

A **Domain Controller (DC)** is a Windows Server that hosts the AD database, answers
authentication requests, and runs the **Kerberos Key Distribution Center (KDC)**.
Domains usually have **two or more DCs** for redundancy; they replicate to each other.

- DCs serve **LDAP** (directory queries, 389/636), **Kerberos** (88), **DNS** (53), and
  **Global Catalog** (3268/3269).
- Compromise a DC and you effectively own the domain — which is exactly why privileged
  access to DCs must be brokered and recorded.

> **Bastion tie-in:** DCs are among the **most critical targets** Bastion protects.
> Bastion talks to a DC for LDAP authentication and (optionally) Kerberos, and admins
> reach the DC *through* Bastion over RDP — never directly.

---

## 3. RDP — Remote Desktop Protocol

**RDP (Remote Desktop Protocol)** is Microsoft's graphical remote-access protocol
(default **TCP port 3389**). It streams the Windows desktop to a client (`mstsc.exe`)
and sends back keyboard/mouse input. Modern RDP adds:

- **NLA (Network Level Authentication):** authenticate *before* a session is created
  (default on in Bastion).
- **TLS (Transport Layer Security):** encrypts the channel.
- **Kerberos:** preferred authentication when available.

> **Bastion tie-in:** Bastion's RDP proxy engine is WALLIX's open-source **"Redemption."**
> Per the [product portfolio](../certs/wallix/overview/product-portfolio.md#session-management),
> Redemption supports **NLA (default on)**, **Kerberos (default on from 12.0.1)**, and
> TLS controls. It records the RDP session as **full-color video**, and the **Session
> Probe** on Windows targets collects rich metadata (window titles, process start/stop,
> clipboard) and **pauses keystroke capture on password fields**. RDP **sub-protocols**
> (clipboard, drive, printer, smartcard, audio) are individually allow/deny per
> authorization.

```mermaid
flowchart LR
    Admin["Admin<br/>mstsc / HTML5<br/>(own identity)"] -->|"RDP leg 1<br/>port 3389 — admin login"| Bastion["WALLIX Bastion<br/>Redemption (proxy)<br/>recorded video + OCR"]
    Bastion -->|"RDP leg 2<br/>port 3389 — injected target account"| Target["Windows target<br/>(DC / server)"]
```

---

## 4. NTLM vs Kerberos

Windows has two authentication protocols. Knowing the difference is core PAM literacy.

| | **NTLM** | **Kerberos** |
|---|---|---|
| Full name | NT LAN Manager | Kerberos (MIT, RFC 4120) |
| Model | Challenge–response, **per-server** | **Ticket-based**, central KDC |
| Crypto | Hash of the password (NT hash) | Symmetric keys + tickets, timestamps |
| Mutual auth | No (client doesn't verify server) | **Yes** |
| Default since | Legacy/fallback | Windows 2000+ (preferred in AD) |
| Known abuses | **Pass-the-Hash**, relay attacks | Kerberoasting, Golden/Silver Ticket |

NTLM is the **legacy fallback**; it sends a challenge-response derived from the password
hash and is vulnerable to **Pass-the-Hash** (stealing the hash to impersonate the user
without knowing the password). Kerberos is the modern default in AD and uses
short-lived **tickets** issued by the DC.

### FLOW: Kerberos authentication (AS-REQ → TGT → TGS → service)

Kerberos has three parties: the **Client**, the **KDC** (Key Distribution Center, running
on the DC, split into an **Authentication Service / AS** and **Ticket-Granting Service /
TGS**), and the **target Service** (e.g., a file server or RDP host).

```mermaid
sequenceDiagram
    participant C as Client (alice)
    participant KDC as KDC on Domain Controller<br/>(AS = Auth Svc, TGS = Ticket-Granting Svc)
    participant SVC as Service (e.g. SRV-DB-01)
    C->>KDC: (1) AS-REQ "I am alice"
    KDC->>C: (2) AS-REP TGT (Ticket-Granting Ticket)<br/>+ session key, encrypted to alice's key
    C->>KDC: (3) TGS-REQ "Give me a ticket for SRV-DB-01"<br/>(present the TGT)
    KDC->>C: (4) TGS-REP Service Ticket for SRV-DB-01
    C->>SVC: (5) AP-REQ present the Service Ticket to the server
    SVC->>C: (6) AP-REP mutual auth OK -> access granted
```

**Plain-English walk-through:**
1. **AS-REQ:** Client asks the KDC's Authentication Service to log in.
2. **AS-REP:** KDC returns a **Ticket-Granting Ticket (TGT)** — a time-limited "proof I
   already authenticated," encrypted so only the KDC can later read it.
3. **TGS-REQ:** To reach a specific service, the client presents the TGT and asks for a
   **service ticket**.
4. **TGS-REP:** KDC issues a **Service Ticket** scoped to that one service.
5. **AP-REQ:** Client presents the Service Ticket directly to the target service.
6. **AP-REP:** Service validates it (and proves its own identity — **mutual auth**);
   access granted. **The password itself is never sent to the service.**

> **Bastion tie-in:** Bastion supports **Kerberos** both as a way users authenticate
> *to* the Bastion and as a way the Bastion authenticates *to* targets. The WCE-P
> (Expert) curriculum covers **"Kerberos Explicit" and "Kerberos Transparent"** as
> advanced authentication modes
> (see [wce-p-expert.md](../certs/wallix/pam-bastion/wce-p-expert.md)). Bastion's RDP proxy uses
> Kerberos by default from version 12.0.1.

---

## 5. Privileged groups and service accounts

### The crown-jewel groups

| Group | Power |
|-------|-------|
| **Domain Admins** | Full control of *the domain* (every member server, every user) |
| **Enterprise Admins** | Full control of *the entire forest* (all domains) |
| **Schema Admins** | Can modify the AD schema itself |
| **Administrators (local)** | Full control of *one machine* |

Membership in these groups is the highest-value prize for an attacker — and the primary
thing PAM exists to govern. Best practice: **keep them nearly empty**, grant access
**Just-in-Time (JIT)**, and broker every use through PAM.

### Service accounts

A **service account** is an account a *program/service* logs in as (e.g., a backup
agent, a database service). They are dangerous because they often have:
- high privilege, and
- **passwords that "never change"** (changing them risks breaking the service), so they
  rot for years.

> **Bastion tie-in:** Bastion's **Password Manager/Vault** is built precisely for this:
> it **vaults and automatically rotates** service-account passwords and SSH keys,
> removing static credentials from scripts and config files. WALLIX markets the
> script/RPA case as **AAPM (Application-to-Application Password Management)**, realized
> via the Bastion REST API + vault plugins (see
> [product portfolio](../certs/wallix/overview/product-portfolio.md#password--secrets-management)).

---

## 6. LAPS — Local Administrator Password Solution

Every Windows machine has a built-in **local Administrator** account. If they all share
the *same* password (a common sin), one stolen password unlocks every machine
(lateral movement). **LAPS (Local Administrator Password Solution)** is Microsoft's
free tool that sets a **unique, random local-admin password per machine** and stores it
securely in AD, rotating it on a schedule.

> **Bastion tie-in:** This is the same *problem* WALLIX solves from the PAM side —
> Bastion vaults and rotates privileged credentials centrally. (On the endpoint side,
> **WALLIX BestSafe** rotates local-account passwords to be *unique per computer, per
> account, per day* — see the
> [product portfolio](../certs/wallix/overview/product-portfolio.md#4-wallix-bestsafe--endpoint-privilege-management-epm).)
> LAPS and PAM are complementary layers of the same least-privilege philosophy.

---

## 7. The Microsoft tiered-admin model

To stop a single compromised admin from cascading into total domain takeover, Microsoft
defines **administrative tiers** that must not cross:

```mermaid
flowchart TD
    T0["Tier 0 — Identity / control plane<br/>(highest)<br/>Domain Controllers, AD, PKI,<br/>Domain/Enterprise Admins<br/>Credentials here can control everything<br/>below"]
    T1["Tier 1 — Servers and applications<br/>Member servers, databases, business apps"]
    T2["Tier 2 — Workstations / end-user devices<br/>(lowest)<br/>Helpdesk, user PCs"]
    T0 --> T1 --> T2
```

> **Rule:** a Tier-0 admin credential must **never** be typed on a Tier-1/2 machine — or it can be stolen and used to climb back up.

The point: credentials of one tier must never be exposed on a lower tier, because a
lower tier is more exposed to compromise.

> **Bastion tie-in:** A PAM broker like Bastion *enforces* tiering operationally. Admins
> connect to a clean broker; the high-tier credential is **injected by the Bastion and
> never lands on the admin's workstation**, so it can't be harvested by malware on a
> lower-tier device. JIT access and session recording reinforce the model.

---

## How this maps to the certifications

- **WCA-P / WCP-P:** RDP and proxy concepts plus AD/LDAP integration are foundational.
- **WCE-P (Expert):** **Advanced authentication** module covers RADIUS, **Kerberos
  Explicit/Transparent**, X.509, and SAML — the AD/Kerberos understanding here is a
  direct prerequisite (see [wce-p-expert.md](../certs/wallix/pam-bastion/wce-p-expert.md)).

---

## Sources

- Microsoft — Active Directory Domain Services overview: https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview
- Microsoft — Group Policy overview: https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831791(v=ws.11)
- RFC 4120 — The Kerberos Network Authentication Service (V5): https://www.rfc-editor.org/rfc/rfc4120
- Microsoft — Kerberos authentication overview: https://learn.microsoft.com/en-us/windows-server/security/kerberos/kerberos-authentication-overview
- Microsoft — NTLM overview: https://learn.microsoft.com/en-us/windows-server/security/windows-authentication/ntlm-overview
- Microsoft — Remote Desktop Protocol: https://learn.microsoft.com/en-us/windows/win32/termserv/remote-desktop-protocol
- Microsoft — Local Administrator Password Solution (Windows LAPS): https://learn.microsoft.com/en-us/windows-server/identity/laps/laps-overview
- Microsoft — Enterprise access model / tiered administration: https://learn.microsoft.com/en-us/security/privileged-access-workstations/privileged-access-access-model
- WALLIX Bastion AD/LDAP, Kerberos, RDP "Redemption": [product-portfolio.md](../certs/wallix/overview/product-portfolio.md) (compiled from WALLIX Bastion 12.3.2 Administration Guide and 12.0.2 Deployment Guide)
