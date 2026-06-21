# Acronyms Reference

> 🔁 This is the **WALLIX / PAM** acronym list. For attack/offensive acronyms, see the
> [CEH acronyms reference](../ceh/reference/acronyms.md).

A comprehensive, exam-oriented reference of the acronyms you will meet across WALLIX
certifications, Privileged Access Management (PAM), the wider identity-security stack,
the protocols and cryptography underneath it, Operational Technology (OT), and the
compliance world. Acronyms are grouped into clearly-headed categories; within each
category they are listed in a table of **Acronym | Expansion | one-line context**.

Where an expansion or behaviour is uncertain or vendor-specific, it is flagged inline
rather than asserted. WALLIX product detail is summarised here and treated
authoritatively in the
[product portfolio](../wallix/overview/product-portfolio.md); the concepts behind these
acronyms are defined in the [glossary](glossary.md) and the
[foundations](../foundations/) folder.

> **How to read certification codes first:** see
> [certification framework](../wallix/overview/certification-framework.md). The decode
> chart below is repeated from there for convenience.

A code reads `W C x - y` (an `e-` prefix marks the self-paced e-learning variant):

| Position | Symbol | Meaning |
|----------|--------|---------|
| 1 | `W` | "WALLIX" |
| 2 | `C` | "Certified" |
| 3 | `x` | **Level:** `A` = Administrator · `P` = Professional · `E` = Expert |
| 4 | `y` | **Track:** `P` = PAM/Bastion · `G` = IAG · `I` = IDaaS · `P-OT` = OT |
| prefix | `e-` | self-paced e-learning variant |

---

## a. WALLIX certifications & codes

| Acronym | Expansion | Context / meaning |
|---|---|---|
| **WCA** | WALLIX Certified Administrator | Entry level: understand and operate the solution day-to-day (no install/deploy). |
| **WCP** | WALLIX Certified Professional | Mid level: install, configure, deploy & administer in a standard architecture. |
| **WCE** | WALLIX Certified Expert | Top level: advanced, large-scale & complex deployments. Requires a prior WCP-P. |
| **WCA-P** | WALLIX Certified Administrator — PAM | Administrator level on the WALLIX Bastion (PAM) track. |
| **WCP-P** | WALLIX Certified Professional — PAM | Professional level on the WALLIX Bastion (PAM) track. |
| **WCE-P** | WALLIX Certified Expert — PAM | Expert level on the Bastion track; requires WCP-P + GNU/Linux CLI knowledge. |
| **WCP-G** | WALLIX Certified Professional — IAG | Professional level on the WALLIX IAG (governance) track (no PAM prerequisite). |
| **WCA-G** | WALLIX Certified Administrator — IAG | Administrator level on the IAG track *(listed as "coming soon")*. |
| **WCP-I** | WALLIX Certified Professional — IDaaS | Professional level on the WALLIX One IDaaS / Trustelem track; requires WCP-P. |
| **WCP-P-OT** | WALLIX Certified Professional — PAM for OT | Professional level on the PAM4OT (Operational Technology) track; requires WCP-P. |
| **-P** (suffix) | PAM / Bastion track | Track suffix for the WALLIX Bastion (Privileged Access Management) product. |
| **-G** (suffix) | IAG track | Track suffix for WALLIX IAG (Identity & Access Governance, ex-Kleverware). |
| **-I** (suffix) | IDaaS track | Track suffix for WALLIX One IDaaS / Trustelem. |
| **-P-OT** (suffix) | PAM-for-OT track | Track suffix for WALLIX PAM4OT (industrial / Operational Technology). |
| **e-** (prefix) | e-learning / self-paced variant | `eWCA-P`, `eWCP-P`, `eWCE-P`, `eWCP-G`, `eWCP-I`, `eWCP-P-OT` are the self-paced WALLIX Academy variants of the instructor-led codes. |
| **MCQ** | Multiple-Choice Questionnaire | The final exam format across current tracks; **≥ 70 %** required to pass. |

> **Code inconsistency to know:** the WALLIX website matrix uses `WCP-G` / `WCP-I` /
> `eWCP-P OT`, while the catalog datasheets use `eWCP-G` / `eWCP-I` / `eWCP-P-OT`. These
> refer to the same certifications. Exam **question count** and **validity/renewal
> period** are *not specified in official sources*.

---

## b. WALLIX products & technologies

| Acronym | Expansion | Context / meaning |
|---|---|---|
| **PAM** | Privileged Access Management | WALLIX's flagship discipline; delivered by **WALLIX Bastion**. Control, vault, broker, record & audit privileged access. |
| **PEDM** | Privilege Elevation & Delegation Management | Elevate a specific command/application rather than the whole user; least privilege at the action level. |
| **EPM** | Endpoint Privilege Management | Remove local-admin rights on endpoints, grant per-app elevation; WALLIX delivers it via **BestSafe**. |
| **IDaaS** | Identity-as-a-Service | Cloud-delivered SSO/MFA/federation; WALLIX delivers it via **Trustelem / WALLIX One IDaaS**. |
| **IAG** | Identity & Access Governance | WALLIX's governance product (acquired **Kleverware**); answers "who *should* have access, and can we prove it?" |
| **IGA** | Identity Governance & Administration | The analyst-preferred name for the same governance discipline as IAG (near-synonyms). |
| **AAPM** | Application-to-Application Password Management | Eliminating hard-coded passwords in scripts/config (DevOps/RPA). *Flag: a marketing term; technically realised via the Bastion REST API + vault plugins.* |
| **WAAPM** | WALLIX AAPM | WALLIX's branding of the Application-to-Application Password Management capability. |
| **WAM** | WALLIX Access Manager | HTML5 web access gateway / reverse proxy in front of one or more Bastions; single secured HTTPS entry point. See [authentication & WAM](../wallix/deep-dives/authentication-and-access-manager.md). |
| **WAB** | WALLIX Bastion (Web Access Bastion) | Internal/legacy product prefix seen in Bastion service names (e.g. `wabgui`, `wabrestapi`, `WABSecurityLevel`). |
| **OT.security** | OT.security by WALLIX | WALLIX brand (launched 2022) for industrial cybersecurity; houses **PAM4OT**. |
| **PAM4OT** | PAM for Operational Technology | OT-specific packaging of WALLIX Bastion for ICS/SCADA/PLC environments. |
| **PAM4ALL** | PAM for All (least-privilege vision) | WALLIX's positioning that pairs PAM (Bastion) + EPM/PEDM (BestSafe) for end-to-end least privilege. |
| **PAG** | Privileged Access Governance | IGA/IAG governance applied specifically to privileged accounts (pairing IAG + Bastion). |
| **UT** | Universal Tunneling | WALLIX Bastion's RAW TCP/IP proxy for arbitrary TCP protocols. |
| **SSPR** | Self-Service Password Reset | Trustelem feature letting users reset their own directory password after verification. |

> See [PAM vs IAM/IGA/IDaaS/EPM](../foundations/pam-iam-iga-idaas-epm.md) for how these
> disciplines overlap, and the
> [product portfolio](../wallix/overview/product-portfolio.md) for product detail.

---

## c. Identity & access

| Acronym | Expansion | Context / meaning |
|---|---|---|
| **IAM** | Identity & Access Management | The broad foundation: manage digital identities and what they may access for the whole workforce. |
| **SSO** | Single Sign-On | Authenticate once, reach many trusting applications via federation (SAML/OIDC). |
| **MFA** | Multi-Factor Authentication | Require two or more independent factors (know / have / are); the top control against stolen passwords. |
| **2FA** | Two-Factor Authentication | MFA with exactly two factors; the common case of MFA. |
| **AuthN** | Authentication | Proving *who you are*. |
| **AuthZ** | Authorization | Determining *what you may do*. |
| **JIT** | Just-In-Time (access) | Grant privileged access only when needed, for a limited time, then auto-revoke. See [core concepts](../foundations/core-concepts-least-privilege-jit-zero-trust.md). |
| **ZSP** | Zero Standing Privileges | End state where no account holds privileged rights at rest; JIT applied everywhere. |
| **SoD** | Separation (Segregation) of Duties | Split a sensitive process so no one person controls all of it; detected as "toxic combinations" in IGA/IAG. |
| **PoLP** | Principle of Least Privilege | Grant the minimum rights needed (NIST SP 800-53 **AC-6**); the foundational rule of access security. |
| **CIEM** | Cloud Infrastructure Entitlement Management | Discover and right-size cloud entitlements/roles for least privilege. *Flag: not a WALLIX product — context only.* |
| **ZTNA** | Zero Trust Network Access | Per-session, per-resource access after verification (vs. a VPN dropping you on the network). |
| **ZTA** | Zero Trust Architecture | The architecture realising Zero Trust; defined in NIST SP 800-207. |
| **RBAC** | Role-Based Access Control | Grant access by assigning users to roles that bundle permissions. |
| **ABAC** | Attribute-Based Access Control | Grant access from attributes/policy (user, resource, context) rather than fixed roles. |
| **A2A** | Application-to-Application | Non-human/machine authentication between apps/services (the use case behind AAPM). |
| **PASM** | Privileged Account & Session Management | Analyst sub-category of PAM: vaulting credentials + brokering/recording sessions (Bastion's core). |
| **JML** | Joiner-Mover-Leaver | The identity lifecycle (onboarding, role change, offboarding) governed by IAM/IGA. |
| **CIAM** | Customer Identity & Access Management | IAM specialised for external customers/consumers (context). |

---

## d. Protocols & directory services

| Acronym | Expansion | Context / meaning |
|---|---|---|
| **SSH** | Secure Shell | Encrypted remote-shell/file protocol (TCP 22); a primary Bastion proxy (with SFTP/sub-systems). |
| **SFTP** | SSH File Transfer Protocol | File transfer over SSH; a controllable SSH sub-protocol in Bastion. |
| **RDP** | Remote Desktop Protocol | Microsoft graphical remote-desktop protocol (TCP 3389); proxied by Bastion's "Redemption" engine. |
| **VNC** | Virtual Network Computing | Cross-platform graphical remote-control protocol; a Bastion proxy. |
| **LDAP** | Lightweight Directory Access Protocol | Directory query/auth protocol (e.g. Active Directory, port 389). |
| **LDAPS** | LDAP over SSL/TLS | Encrypted LDAP (port 636). |
| **AD** | Active Directory | Microsoft's directory service; a key external authentication source for Bastion, Trustelem & BestSafe. |
| **RADIUS** | Remote Authentication Dial-In User Service | AAA / network-auth protocol (UDP 1812); common MFA "second-factor" channel. |
| **TACACS+** | Terminal Access Controller Access-Control System Plus | Cisco AAA protocol for device administration (separates authN/authZ/accounting). |
| **SAML** | Security Assertion Markup Language | XML-based SSO/federation standard (v2.0); WAM can act as a SAML Service Provider. |
| **OIDC** | OpenID Connect | Identity layer on top of OAuth 2.0 for SSO; supported by WAM (Authorization Code Flow) and Trustelem. |
| **OAuth** | Open Authorization | Delegated-authorization framework (v2.0) underlying OIDC. |
| **SCIM** | System for Cross-domain Identity Management | Standard for provisioning/deprovisioning users & groups across apps (v2.0; Trustelem is a SCIM client). |
| **SNMP** | Simple Network Management Protocol | Monitoring protocol (v2c/v3) supported by Bastion for health/metrics. |
| **Syslog** | System Logging Protocol | Standard event-logging transport (port 514); Bastion forwards to SIEM via `syslog-ng`. |
| **NLA** | Network Level Authentication | RDP pre-authentication (default on in Bastion's RDP proxy) that authenticates before a full session. |
| **Kerberos** | (not an acronym) | Ticket-based network authentication protocol; supported in Bastion's RDP/directory integration. |
| **TELNET** | Telecommunication Network | Legacy unencrypted remote-terminal protocol; proxied/recorded by Bastion (common in OT). |
| **RLOGIN** | Remote Login | Legacy Unix remote-login protocol; a Bastion proxy. |
| **DNS** | Domain Name System | Name-to-IP resolution; relevant to target addressing (FQDN) and appliance networking. |
| **FQDN** | Fully Qualified Domain Name | A complete host name; one way to define a Bastion device/target. |
| **CIDR** | Classless Inter-Domain Routing | IP subnet notation (e.g. `10.0.0.0/24`); one way to define a Bastion device by subnet. |

---

## e. Cryptography & PKI

| Acronym | Expansion | Context / meaning |
|---|---|---|
| **TLS** | Transport Layer Security | Modern encryption-in-transit protocol (successor to SSL); secures HTTPS/LDAPS, etc. |
| **SSL** | Secure Sockets Layer | Legacy predecessor to TLS; the term persists colloquially ("SSL certificate"). |
| **PKI** | Public Key Infrastructure | The system of CAs, certificates and revocation that binds keys to identities. |
| **CA** | Certificate Authority | Trusted issuer that signs digital certificates. |
| **CSR** | Certificate Signing Request | A request (containing a public key) submitted to a CA to obtain a certificate. |
| **CRL** | Certificate Revocation List | A published list of revoked certificates; WAM can check it for X.509 auth. |
| **OCSP** | Online Certificate Status Protocol | Real-time certificate-revocation check (alternative to a CRL). |
| **AES** | Advanced Encryption Standard | Symmetric cipher; Bastion uses **AES-256** (encryption at rest/in transit). |
| **RSA** | Rivest–Shamir–Adleman | Public-key algorithm; Bastion defaults to large RSA keys (≥ 3072-bit; 4096 for rotated SSH keys). |
| **ECDSA** | Elliptic Curve Digital Signature Algorithm | Elliptic-curve signature algorithm; supported for SSH key generation in Bastion. |
| **ECC** | Elliptic Curve Cryptography | The family of curve-based public-key crypto (e.g. ECDSA); used by Bastion. |
| **DSA** | Digital Signature Algorithm | Older signature algorithm; supported for SSH key generation in Bastion (RSA/ECDSA preferred). |
| **SHA** | Secure Hash Algorithm | Cryptographic hash family; Bastion uses **SHA-2**. |
| **LUKS** | Linux Unified Key Setup | Linux disk-encryption standard (dm-crypt); Bastion's encryption at rest. |
| **TOTP** | Time-based One-Time Password | OTP derived from a shared secret + current time (RFC 6238); a Trustelem MFA factor. |
| **HOTP** | HMAC-based One-Time Password | Counter-based OTP (RFC 4226); the precursor to TOTP. |
| **OTP** | One-Time Password | A single-use code; delivered via TOTP/HOTP, SMS, or email. |
| **HMAC** | Hash-based Message Authentication Code | Keyed-hash integrity/authentication construct underlying HOTP/TOTP. |
| **FIDO** | Fast IDentity Online | Passwordless/strong-auth standards body & protocols (FIDO U2F, **FIDO2**). |
| **FIDO2** | FIDO second-generation standard | Phishing-resistant auth using hardware keys (e.g. YubiKey) via WebAuthn + CTAP. |
| **WebAuthn** | Web Authentication | W3C browser API for FIDO2 hardware-key authentication; a Trustelem MFA option. |
| **CTAP** | Client to Authenticator Protocol | The FIDO2 companion to WebAuthn linking browser/OS to the security key. |
| **GPG** | GNU Privacy Guard | OpenPGP implementation; Bastion uses GPG to encrypt nightly credential exports and sign ISOs. |
| **PGP** | Pretty Good Privacy | The encryption standard GPG implements (OpenPGP). |

> **Crypto policy note:** Bastion's cryptographic level is selectable via
> `WABSecurityLevel`, with **SOG-IS CES 1.3** (valid to 2030) recommended. See
> [Bastion architecture](../wallix/deep-dives/bastion-architecture.md) and
> [secrets & password management](../wallix/deep-dives/secrets-and-password-management.md).

---

## f. OT / industrial

| Acronym | Expansion | Context / meaning |
|---|---|---|
| **OT** | Operational Technology | Hardware/software that monitors & controls physical processes (factories, utilities); the domain of PAM4OT. |
| **IT** | Information Technology | The conventional enterprise computing domain; contrasted with OT at the IT/OT boundary. |
| **ICS** | Industrial Control System | Umbrella term for control systems (SCADA, DCS, PLCs) running industrial processes. |
| **SCADA** | Supervisory Control And Data Acquisition | Systems that supervise and acquire data from geographically distributed industrial assets. |
| **DCS** | Distributed Control System | Process-control system with controllers distributed across a plant (context). |
| **PLC** | Programmable Logic Controller | Ruggedised industrial computer controlling machinery; an OT target (cannot host agents → agentless PAM). |
| **RTU** | Remote Terminal Unit | Field device that collects telemetry and relays it to SCADA; an OT target. |
| **HMI** | Human-Machine Interface | Operator screen/console for an industrial process; an OT target often reached over RDP/VNC. |
| **DMZ** | Demilitarized Zone | A buffer network between trust zones; an **Industrial DMZ** sits between IT and OT (Purdue Level 3.5) where a PAM jump host lives. |
| **IIoT** | Industrial Internet of Things | Networked industrial sensors/devices (context for OT attack surface). |
| **Modbus** | (not an acronym) | Common industrial protocol; can be encapsulated in an SSH tunnel by PAM4OT for traceable PLC access. |
| **LPM** | Loi de Programmation Militaire | France's military-programming law imposing security obligations on critical operators (cited in WALLIX OT messaging). |

> See the OT discussion in the
> [product portfolio PAM4OT section](../wallix/overview/product-portfolio.md#6-wallix-pam4ot--operational-technology-ot-security).

---

## g. Compliance, standards & bodies

| Acronym | Expansion | Context / meaning |
|---|---|---|
| **NIS2** | Network and Information Security Directive 2 | EU directive (2022/2555) raising cybersecurity obligations for essential/important entities. |
| **IEC** | International Electrotechnical Commission | Standards body publishing IEC 62443 (with ISA), IEC 27001 alignment, etc. |
| **ISA** | International Society of Automation | Co-author of the ISA/IEC 62443 OT-security series. |
| **62443** | ISA/IEC 62443 | The leading **OT/ICS** security standard series (zones & conduits, security levels). |
| **DORA** | Digital Operational Resilience Act | EU regulation (2022/2554) on ICT operational resilience for the financial sector. |
| **GDPR** | General Data Protection Regulation | EU regulation (2016/679) on personal-data protection; drives access control & auditability. |
| **ISO** | International Organization for Standardization | Standards body; co-publishes ISO/IEC 27001 with the IEC. |
| **ISO 27001** | ISO/IEC 27001 | International standard for Information Security Management Systems (ISMS). WALLIX holds 27001:2022. |
| **ISMS** | Information Security Management System | The managed framework of policies/controls that ISO 27001 certifies. |
| **PCI DSS** | Payment Card Industry Data Security Standard | Card-data protection standard; strict on privileged access, MFA, logging & unique IDs. |
| **SOX** | Sarbanes-Oxley Act | US law on financial reporting integrity; drives access controls & SoD over financial systems. |
| **HIPAA** | Health Insurance Portability and Accountability Act | US healthcare law; its Security Rule governs access control & audit of electronic PHI. |
| **PHI** | Protected Health Information | The health data HIPAA protects (context). |
| **NERC CIP** | North American Electric Reliability Corporation — Critical Infrastructure Protection | Mandatory standards for the North American bulk electric system (strong on electronic access & logging). |
| **NIST** | National Institute of Standards and Technology | US body publishing the CSF and the SP 800 series. |
| **CSF** | Cybersecurity Framework | NIST's voluntary framework (Identify/Protect/Detect/Respond/Recover, + Govern in CSF 2.0). |
| **SP** | Special Publication | NIST document series (e.g. **SP 800-53**, **SP 800-82**, **SP 800-171**, **SP 800-207**). |
| **ANSSI** | Agence nationale de la sécurité des systèmes d'information | France's national cybersecurity agency; issues the **CSPN** certification. |
| **BSI** | Bundesamt für Sicherheit in der Informationstechnik | Germany's federal cybersecurity office; issues the **BSZ** certification. |
| **CSPN** | Certification de Sécurité de Premier Niveau | ANSSI's first-level security certification; awarded to WALLIX Bastion. |
| **BSZ** | Beschleunigte Sicherheitszertifizierung | BSI's accelerated security certification; obtained by WALLIX (mutually recognised by ANSSI ~late 2025). |
| **ENISA** | European Union Agency for Cybersecurity | EU agency supporting cybersecurity policy/implementation (e.g. NIS2 guidance). |
| **SOG-IS** | Senior Officials Group — Information Systems Security | European group behind crypto-evaluation agreements; Bastion can target **SOG-IS CES 1.3** crypto. |
| **CC** | Common Criteria | International security-evaluation framework (ISO/IEC 15408). *Flag: no specific WALLIX EAL level confirmed.* |
| **EAL** | Evaluation Assurance Level | Common Criteria assurance rating (EAL1–7). *Flag: no EAL level confirmed for WALLIX Bastion in sources.* |
| **CIS** | Center for Internet Security | Publisher of the CIS Controls / Benchmarks (hardening guidance; context). |

> Full mapping of how PAM supports each of these is in
> [compliance & standards](compliance-and-standards.md).

---

## h. Operations & infrastructure

| Acronym | Expansion | Context / meaning |
|---|---|---|
| **HA** | High Availability | Resilient configuration avoiding single points of failure; Bastion v12 HA = DB replication. See [HA & DR](../wallix/deep-dives/high-availability-and-dr.md). |
| **DR** | Disaster Recovery | The capability to restore service after a major outage/disaster. |
| **DRP** | Disaster Recovery Plan | The documented procedure executing DR (objectives, steps, roles). |
| **RPO** | Recovery Point Objective | Max acceptable data loss (time) in a disaster — relevant to Bastion replication scope. |
| **RTO** | Recovery Time Objective | Max acceptable downtime before service is restored. |
| **SIEM** | Security Information and Event Management | Central log/event correlation platform; Bastion forwards events via Syslog. |
| **SOAR** | Security Orchestration, Automation and Response | Automates incident response on top of SIEM (context for API-driven PAM actions). |
| **UEBA** | User and Entity Behavior Analytics | Anomaly detection from user/entity behaviour (WALLIX's Malizen acquisition area). |
| **API** | Application Programming Interface | Programmatic interface; Bastion exposes a **REST API** (`wabrestapi`). See [REST API & automation](../wallix/deep-dives/rest-api-and-automation.md). |
| **REST** | Representational State Transfer | The architectural style of Bastion's HTTP/JSON API. |
| **JSON** | JavaScript Object Notation | The data format used by the Bastion REST API. |
| **ETL** | Extract, Transform, Load | Data-integration pattern; WALLIX IAG uses an ETL to consolidate identity data from many sources. |
| **OVA** | Open Virtual Appliance / Open Virtualization Archive | Packaged virtual-machine image; format of WALLIX Academy e-learning lab images. |
| **OVF** | Open Virtualization Format | The standard an OVA packages a VM in. |
| **VM** | Virtual Machine | Software-emulated computer; Bastion/WAM ship as virtual appliances for major hypervisors/clouds. |
| **ISO** | ISO disk image | A bootable image; Bastion is also distributed as a GPG-signed ISO. *(Distinct from ISO the standards body.)* |
| **GUI** | Graphical User Interface | Bastion's admin web GUI (`wabgui`). |
| **CLI** | Command-Line Interface | Text command interface; e.g. the `bastion-replication` CLI for HA. |
| **LVM** | Logical Volume Manager | Linux volume manager; Bastion stores data/recordings on LVM (`/var/wab`), extendable for retention. |
| **DRBD** | Distributed Replicated Block Device | Block-level replication; **removed** in Bastion v12 in favour of DB replication. |
| **SLA** | Service Level Agreement | Contractual availability/performance commitment (WALLIX One PAM SaaS: 99.9 % uptime). |
| **SaaS** | Software-as-a-Service | Cloud subscription delivery model; **WALLIX One** is WALLIX's SaaS platform. |
| **MSP** | Managed Service Provider | Outsourced IT/security provider; a WALLIX One channel audience. |
| **ITSM** | IT Service Management | Ticketing/service platforms integrated for approval workflows & IAG remediation. |
| **KPI** | Key Performance Indicator | Metric surfaced in Bastion's Superset dashboards for audit/activity reporting. |
| **DC** | Domain Controller | Active Directory server; the BestSafe agent contacts the closest DC. |
| **GPO** | Group Policy Object | Windows/AD policy mechanism; BestSafe distributes policy in an AD/GPO-style manner. |
| **MMC** | Microsoft Management Console | Windows admin console; BestSafe is managed via an MMC snap-in. |

---

## See also

- [Glossary](glossary.md) — plain-language definitions of the concepts behind these acronyms.
- [Compliance & standards](compliance-and-standards.md) — how PAM maps to each framework.
- [PAM vs IAM/IGA/IDaaS/EPM](../foundations/pam-iam-iga-idaas-epm.md)
- [Core concepts: least privilege, JIT, Zero Trust](../foundations/core-concepts-least-privilege-jit-zero-trust.md)
- [WALLIX product portfolio](../wallix/overview/product-portfolio.md)
- [Certification framework](../wallix/overview/certification-framework.md)

---

## Sources

- WALLIX Academy / certification framework (this repo): [../docs/00-overview/certification-framework.md](../wallix/overview/certification-framework.md); WALLIX Academy: https://www.wallix.com/support-services/wallix-academy/; Training catalog 2025–2026 (EN): https://www.wallix.com/wp-content/uploads/2024/04/WALLIX_TRAINING_2025-2026_ENG.pdf
- WALLIX product portfolio (this repo, with primary WALLIX sources): [../docs/00-overview/product-portfolio.md](../wallix/overview/product-portfolio.md)
- WALLIX Bastion Administration Guide (served v12.3.2): https://pam.wallix.one/documentation/admin-doc/bastion_en_administration_guide.pdf
- WALLIX Bastion Deployment Guide (v12.0.2): https://marketplace-wallix.s3.amazonaws.com/bastion_12.0.2_en_deployment_guide.pdf
- WALLIX Access Manager Administration Guide (served v5.2.4.0): https://pam.wallix.one/documentation/admin-doc/am-admin-guide_en.pdf
- WALLIX Trustelem documentation (MFA factors, SCIM, RADIUS/LDAP): https://trustelem-doc.wallix.com/
- NIST SP 800-53 Rev. 5 (AC-6 least privilege): https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
- NIST SP 800-207 Zero Trust Architecture: https://csrc.nist.gov/pubs/sp/800/207/final
- NIST Cybersecurity Framework 2.0: https://www.nist.gov/cyberframework
- ISA/IEC 62443 series overview (ISA): https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards
- IETF — TOTP (RFC 6238): https://www.rfc-editor.org/rfc/rfc6238 · HOTP (RFC 4226): https://www.rfc-editor.org/rfc/rfc4226
- FIDO Alliance — FIDO2 / WebAuthn / CTAP: https://fidoalliance.org/fido2/
- ANSSI — CSPN: https://cyber.gouv.fr/la-certification-de-securite-de-premier-niveau-cspn
- BSI — BSZ (Beschleunigte Sicherheitszertifizierung): https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/Zertifizierung-und-Anerkennung/
