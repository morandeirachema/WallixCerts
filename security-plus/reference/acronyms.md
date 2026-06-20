# Security+ Acronyms Reference

> 🔁 This is the **CompTIA Security+ (SY0-701)** acronym list. For offensive / ethical-hacking acronyms see the [CEH acronyms reference](../../ceh/reference/acronyms.md); for PAM, identity & WALLIX acronyms see the [WALLIX acronyms reference](../../reference/acronyms.md). The three lists overlap heavily (cryptography, protocols, governance) and are complementary, not duplicated — where an entry is treated in more depth in another hub, that is noted.

CompTIA Security+ is famous for its **long official acronym list**: the exam objectives end with an acronym appendix you are expected to recognise on sight. This page is a comprehensive, categorised reference covering that list (and a few closely-adjacent terms). Each table gives the **acronym**, its **expansion**, and a **one-line context** in Security+ terms. Acronyms are expanded on first use throughout the hub; this page is the master list.

> **Verify against the source.** The authoritative list is the acronym appendix in CompTIA's official **SY0-701 exam objectives** PDF (download link on the [Security+ page](https://www.comptia.org/en-us/certifications/security/)). Where an acronym has more than one common expansion, the **security-relevant** meaning is given. Algorithm/standard facts are anchored to the **NIST glossary** and primary specifications — see [Sources](#sources). For prose definitions, see the [glossary](glossary.md).

> Tip for a sysadmin: skim the **Networking, protocols & ports** and **Security operations & monitoring** tables first — most of that vocabulary you already know from administration; Security+ simply names and groups it.

## Contents

- [Cryptography, PKI & hashing](#cryptography-pki--hashing)
- [Authentication, identity & access](#authentication-identity--access)
- [Networking, protocols & ports](#networking-protocols--ports)
- [Security operations & monitoring](#security-operations--monitoring)
- [Email & web security](#email--web-security)
- [Governance, risk & compliance](#governance-risk--compliance)
- [Cloud & virtualization](#cloud--virtualization)
- [Wireless & mobile](#wireless--mobile)
- [Physical, IoT & OT](#physical-iot--ot)
- [Incident response, forensics & resilience](#incident-response-forensics--resilience)
- [Attacks, vulnerabilities & threats](#attacks-vulnerabilities--threats)

## Cryptography, PKI & hashing

Maps mainly to **Domain 1 (General Security Concepts)** cryptographic solutions. Overlaps the [CEH](../../ceh/reference/acronyms.md#cryptography) and [WALLIX](../../reference/acronyms.md) lists.

| Acronym | Expansion | Context |
| --- | --- | --- |
| AES | Advanced Encryption Standard | The dominant symmetric block cipher (128/192/256-bit keys); NIST FIPS 197. |
| DES | Data Encryption Standard | Legacy symmetric cipher, insecure due to its 56-bit key. |
| 3DES | Triple Data Encryption Standard (Triple DEA) | Runs DES three times to extend strength; now deprecated by NIST. |
| RC4 | Rivest Cipher 4 | Legacy stream cipher (used by WEP/old TLS); now considered insecure. |
| RSA | Rivest–Shamir–Adleman | Widely used public-key algorithm for encryption and digital signatures. |
| DH | Diffie–Hellman | Key-exchange algorithm letting two parties derive a shared secret over an open channel. |
| DHE | Diffie–Hellman Ephemeral | DH using per-session (ephemeral) keys to provide forward secrecy. |
| ECC | Elliptic Curve Cryptography | Public-key cryptography giving strong security with smaller keys. |
| ECDSA | Elliptic Curve Digital Signature Algorithm | ECC-based digital-signature algorithm. |
| ECDHE | Elliptic Curve Diffie–Hellman Ephemeral | Ephemeral DH over elliptic curves; the common forward-secret TLS key exchange. |
| PFS | Perfect Forward Secrecy | Property where compromise of a long-term key does not expose past session keys. |
| SHA | Secure Hash Algorithm | Hash-function family (SHA-1 deprecated; SHA-2/SHA-3 current). |
| HMAC | Hash-based Message Authentication Code | Hash + secret key proving integrity **and** authenticity of a message. |
| MD5 | Message Digest 5 | Legacy 128-bit hash, broken for collision resistance; non-security checksums only. |
| PKI | Public Key Infrastructure | Framework of keys, certificates and authorities underpinning TLS, signing, etc. |
| CA | Certificate Authority | Trusted issuer of digital certificates within a PKI. |
| RA | Registration Authority | Vets and approves certificate requests on behalf of a CA. |
| CRL | Certificate Revocation List | Signed list of certificates revoked before their expiry. |
| OCSP | Online Certificate Status Protocol | Real-time query of a single certificate's revocation status (alternative to a CRL). |
| CSR | Certificate Signing Request | Request submitted to a CA to obtain a signed certificate. |
| OID | Object Identifier | A dotted-number identifier used in certificates (e.g. for policies/extensions). |
| SAN | Subject Alternative Name | Certificate field listing additional hostnames/identities the cert covers. |
| CN | Common Name | The primary subject name field of a certificate (largely superseded by SAN). |
| DER / PEM / PFX / P12 / CER | Certificate encodings/containers | Common X.509 file formats: DER (binary), PEM (Base64), PFX/P12 (PKCS#12 bundle), CER (cert file). |
| TPM | Trusted Platform Module | On-board crypto chip storing keys/measurements; supports secure boot and FDE. |
| HSM | Hardware Security Module | Tamper-resistant device that generates, stores and uses keys. |
| KEK / DEK | Key Encryption Key / Data Encryption Key | A KEK encrypts (wraps) the DEK that actually encrypts data — common in envelope encryption. |
| FDE | Full Disk Encryption | Encrypts an entire drive so data at rest is unreadable without the key. |
| SED | Self-Encrypting Drive | Drive that performs encryption in hardware on its own controller. |
| OTP | One-Time Password | A password valid for a single login/transaction (umbrella over HOTP/TOTP). |
| TOTP | Time-based One-Time Password | Time-synced one-time code (authenticator apps) used as a second factor. |
| HOTP | HMAC-based One-Time Password | Counter-based one-time-password scheme (the basis TOTP builds on). |
| PGP / GPG | Pretty Good Privacy / GNU Privacy Guard | Software/standard (and its open-source implementation) for encrypting and signing data and email. |
| S/MIME | Secure/Multipurpose Internet Mail Extensions | Standard for signing and encrypting email using X.509 certificates. |
| DRM | Digital Rights Management | Controls restricting use/copying of digital content. |
| DSA | Digital Signature Algorithm | NIST signature algorithm (predecessor to ECDSA in common use). |
| CBC / GCM / ECB | Cipher Block Chaining / Galois-Counter Mode / Electronic Code Book | Block-cipher modes of operation; GCM adds authentication (AEAD), ECB is insecure for bulk data. |

## Authentication, identity & access

Maps mainly to **Domain 1** (cryptography/access concepts) and **Domain 4 (Security Operations)** identity management. Overlaps the [WALLIX identity glossary](../../reference/glossary.md).

| Acronym | Expansion | Context |
| --- | --- | --- |
| AAA | Authentication, Authorization, and Accounting | The three pillars of access control: who you are, what you may do, and recording it. |
| IAM | Identity and Access Management | Discipline/tooling for managing identities and their access. |
| IdP | Identity Provider | Service that authenticates users and asserts identity to relying parties (SAML/OIDC). |
| SSO | Single Sign-On | Authenticate once and reach many trusting apps via federation. |
| MFA | Multi-Factor Authentication | Requiring two or more independent factors (know / have / are / somewhere you are). |
| 2FA | Two-Factor Authentication | MFA with exactly two factors (e.g. password + OTP). |
| RADIUS | Remote Authentication Dial-In User Service | AAA protocol commonly used for network/VPN/Wi-Fi authentication (UDP 1812/1813). |
| TACACS+ | Terminal Access Controller Access-Control System Plus | Cisco AAA protocol that separates AuthN/AuthZ/Accounting; encrypts the whole payload (TCP 49). |
| LDAP | Lightweight Directory Access Protocol | Queries directory services such as Active Directory (TCP/UDP 389; LDAPS 636). |
| LDAPS | LDAP over SSL/TLS | LDAP wrapped in TLS for confidentiality (TCP 636). |
| SAML | Security Assertion Markup Language | XML standard for exchanging authentication/authorization assertions in federated SSO. |
| OAuth | Open Authorization | Delegated-**authorization** framework letting an app access resources on a user's behalf. |
| OIDC | OpenID Connect | Identity (**authentication**) layer built on top of OAuth 2.0. |
| PAM | Privileged Access Management | Controlling, vaulting and auditing privileged accounts — the [WALLIX hub](../../README.md) topic. |
| PAM | Pluggable Authentication Modules | (Linux) Framework for plugging authentication methods into services — context disambiguates from the above. |
| RBAC | Role-Based Access Control | Granting access via roles that bundle permissions. |
| ABAC | Attribute-Based Access Control | Granting access from evaluated attributes (user, resource, environment). |
| MAC | Mandatory Access Control | System-enforced access by labels/clearances; users cannot change permissions. |
| DAC | Discretionary Access Control | Owners set permissions on their own objects at their discretion. |
| RBAC | Rule-Based Access Control | Access decided by admin-defined rules (e.g. ACL/firewall rules) — distinct from Role-Based. |
| EAP | Extensible Authentication Protocol | Authentication framework (many methods) used in 802.1X / wireless. |
| PEAP | Protected EAP | EAP variant tunnelling authentication inside a TLS tunnel. |
| CHAP | Challenge-Handshake Authentication Protocol | Challenge/response auth that avoids sending the password in clear. |
| PAP | Password Authentication Protocol | Legacy auth that sends credentials in cleartext; insecure. |
| Kerberos | Kerberos (not an acronym) | Ticket-based network authentication protocol used by Active Directory (TCP/UDP 88). |
| KDC | Key Distribution Center | The Kerberos service issuing tickets (TGT/service tickets). |
| TGT | Ticket-Granting Ticket | Kerberos ticket used to request service tickets after initial logon. |
| SID | Security Identifier | Unique identifier assigned to Windows security principals. |
| FIDO | Fast IDentity Online | Standards (FIDO2/WebAuthn) for phishing-resistant, passwordless authentication. |
| FAR / FRR / CER | False Acceptance Rate / False Rejection Rate / Crossover Error Rate | Biometric accuracy metrics; CER is where FAR and FRR are equal (lower = better). |
| JIT | Just-in-Time (provisioning/access) | Granting accounts/privileges only at the moment of need, then revoking. |
| ACL | Access Control List | Ordered rules deciding which subjects may access which objects (also a firewall term). |

## Networking, protocols & ports

Maps mainly to **Domain 3 (Security Architecture)** and **Domain 4**. Default ports are common assignments; services can be reconfigured. Overlaps the [CEH protocols table](../../ceh/reference/acronyms.md#protocols--ports).

| Acronym | Expansion | Context (default port) |
| --- | --- | --- |
| TCP | Transmission Control Protocol | Connection-oriented, reliable transport (Layer 4). |
| UDP | User Datagram Protocol | Connectionless, lightweight transport (Layer 4). |
| IP | Internet Protocol | Layer-3 addressing/routing protocol (IPv4 and IPv6). |
| DNS | Domain Name System | Resolves names to IP addresses; a recon target and exfiltration channel (UDP/TCP 53). |
| DNSSEC | DNS Security Extensions | Adds origin authentication/integrity to DNS records via signatures. |
| DHCP | Dynamic Host Configuration Protocol | Assigns IP configuration automatically; abused via rogue servers (UDP 67/68). |
| HTTP | HyperText Transfer Protocol | Unencrypted web protocol (TCP 80). |
| HTTPS | HTTP Secure | HTTP wrapped in TLS (TCP 443). |
| FTP | File Transfer Protocol | Cleartext file transfer; credentials sniffable (TCP 20/21). |
| FTPS | FTP Secure | FTP over TLS. |
| SFTP | SSH File Transfer Protocol | File transfer over an SSH channel (TCP 22). |
| TFTP | Trivial File Transfer Protocol | Minimal, unauthenticated file transfer (UDP 69). |
| SSH | Secure Shell | Encrypted remote shell and tunnelling (TCP 22). |
| TLS | Transport Layer Security | Modern protocol encrypting HTTPS and many services. |
| SSL | Secure Sockets Layer | Deprecated predecessor to TLS; still loosely used for "the encryption layer." |
| IPSec | Internet Protocol Security | Suite securing IP traffic (AH/ESP); the basis of many VPNs. |
| AH / ESP | Authentication Header / Encapsulating Security Payload | IPSec protocols: AH gives integrity/authentication, ESP adds confidentiality. |
| IKE | Internet Key Exchange | Negotiates IPSec security associations and keys. |
| VPN | Virtual Private Network | Encrypted tunnel extending a private network over an untrusted one. |
| VLAN | Virtual Local Area Network | Logical Layer-2 segment used to isolate traffic on shared switches. |
| NAT | Network Address Translation | Rewrites IP addresses between networks (often private↔public). |
| PAT | Port Address Translation | NAT variant mapping many hosts to one IP via ports (overload). |
| NAC | Network Access Control | Enforces policy on which devices may join a network and under what conditions. |
| SDN | Software-Defined Networking | Decouples the network control plane from the data plane for programmable control. |
| SD-WAN | Software-Defined Wide Area Network | Software-managed WAN overlay across multiple links/providers. |
| SASE | Secure Access Service Edge | Cloud model converging SD-WAN with security (SWG, CASB, ZTNA, FWaaS). |
| ACL | Access Control List | Ordered rules on a router/firewall permitting or denying traffic. |
| BGP | Border Gateway Protocol | The internet's inter-domain routing protocol; route hijacking is a threat. |
| ICMP | Internet Control Message Protocol | Diagnostics/error messaging (e.g. ping); used in discovery and some tunnelling (Layer 3). |
| SNMP | Simple Network Management Protocol | Manages/monitors devices; weak community strings leak data (UDP 161/162). |
| NTP | Network Time Protocol | Time synchronisation; abused in DDoS amplification (UDP 123). |
| SMTP | Simple Mail Transfer Protocol | Sends email (TCP 25; submission 587; SMTPS 465). |
| IMAP | Internet Message Access Protocol | Retrieves email, leaving it on the server (TCP 143; IMAPS 993). |
| POP3 | Post Office Protocol v3 | Retrieves email, typically downloading and removing it (TCP 110; POP3S 995). |
| RDP | Remote Desktop Protocol | Windows remote graphical access; brute-force/lateral-movement target (TCP 3389). |
| SMB | Server Message Block | Windows file/printer sharing (TCP 445). |
| MAC (address) | Media Access Control address | Hardware address identifying a NIC at Layer 2 (spoofable). |
| GRE | Generic Routing Encapsulation | Tunnelling protocol that encapsulates many protocols (often paired with IPSec). |
| QoS | Quality of Service | Traffic prioritisation; relevant to availability and DoS resilience. |
| PtP / P2P | Point-to-Point / Peer-to-Peer | Direct link between two nodes / decentralised node-to-node networking. |

## Security operations & monitoring

Maps mainly to **Domain 4 (Security Operations, 28%)**. Overlaps the [CEH defence table](../../ceh/reference/acronyms.md#defense--operations).

| Acronym | Expansion | Context |
| --- | --- | --- |
| SIEM | Security Information and Event Management | Aggregates and correlates logs/events for detection and investigation; central to a SOC. |
| SOAR | Security Orchestration, Automation, and Response | Automates and coordinates SOC workflows and playbooks. |
| SOC | Security Operations Center | The team/facility that monitors, detects and responds to security events. |
| EDR | Endpoint Detection and Response | Agent-based tooling monitoring endpoints for malicious behaviour and enabling response. |
| XDR | Extended Detection and Response | Correlates detection/response across endpoints, network, identity and cloud. |
| MDR | Managed Detection and Response | Outsourced, vendor-run detection-and-response service. |
| DLP | Data Loss Prevention | Controls that detect and block sensitive data leaving the organisation. |
| IDS | Intrusion Detection System | Monitors traffic/hosts and **alerts** on suspicious activity. |
| IPS | Intrusion Prevention System | Like an IDS but can **block** detected threats inline. |
| NIDS / NIPS | Network-based IDS / IPS | Inspects (and for NIPS, blocks) traffic on a network segment. |
| HIDS / HIPS | Host-based IDS / IPS | Runs on and protects a single host. |
| WAF | Web Application Firewall | Filters HTTP(S) traffic to protect web apps from SQLi, XSS, etc. |
| UTM | Unified Threat Management | Single appliance combining firewall, IPS, antivirus and more. |
| NGFW | Next-Generation Firewall | Firewall adding app awareness, IPS and identity-based policy. |
| FIM | File Integrity Monitoring | Detects unauthorised changes to critical files via baselining/hashing. |
| UEBA | User and Entity Behavior Analytics | Detects anomalies by modelling normal user/entity behaviour. |
| IoC | Indicator of Compromise | Forensic evidence (hashes, IPs, domains) suggesting a breach. |
| TTP | Tactics, Techniques, and Procedures | The behavioural "fingerprint" of an adversary (e.g. mapped in MITRE ATT&CK). |
| OSINT | Open-Source Intelligence | Intelligence gathered from publicly available sources. |
| MTTR | Mean Time To Repair / Respond / Recover | Average time to restore service or respond to an incident (lower is better). |
| TAXII / STIX | Trusted Automated eXchange of Indicator Information / Structured Threat Information eXpression | Standards for sharing (STIX) and transporting (TAXII) cyber-threat intelligence. |
| HoneyPot / HoneyNet | (not acronyms) | A decoy host / decoy network used to detect and study attackers. |
| GPO | Group Policy Object | Windows mechanism for centrally enforcing security configuration. |
| SCAP | Security Content Automation Protocol | NIST suite of standards for automating configuration/vulnerability assessment. |
| CVE | Common Vulnerabilities and Exposures | Public catalogue assigning unique IDs to known vulnerabilities. |
| CVSS | Common Vulnerability Scoring System | Standard 0–10 severity score for vulnerabilities. |
| SOC (report) | System and Organization Controls | An AICPA audit-report type (e.g. SOC 2) — distinct from Security Operations Center. |

## Email & web security

Maps to **Domain 2 (Threats)** and **Domain 4**. Overlaps the [CEH web table](../../ceh/reference/acronyms.md#web--application).

| Acronym | Expansion | Context |
| --- | --- | --- |
| SPF | Sender Policy Framework | DNS record listing hosts allowed to send mail for a domain (anti-spoofing). |
| DKIM | DomainKeys Identified Mail | Cryptographically signs outbound mail so receivers can verify it was not altered. |
| DMARC | Domain-based Message Authentication, Reporting and Conformance | Policy built on SPF + DKIM telling receivers how to handle failures and where to report. |
| XSS | Cross-Site Scripting | Injecting attacker script into pages other users view. |
| CSRF / XSRF | Cross-Site Request Forgery | Tricking a logged-in user's browser into sending unwanted authenticated requests. |
| SQLi | SQL Injection | Injecting attacker-controlled SQL into a query. |
| CSP | Content Security Policy | HTTP header restricting which resources a page may load (mitigates XSS). |
| CORS | Cross-Origin Resource Sharing | Browser mechanism relaxing the Same-Origin Policy; misconfiguration leaks data. |
| API | Application Programming Interface | The contract through which software components talk; a growing attack surface. |
| URL / URI | Uniform Resource Locator / Identifier | Web address; URL parsing/redirection abuse is a phishing vector. |
| HSTS | HTTP Strict Transport Security | Header forcing browsers to use HTTPS for a site. |
| OWASP | Open Worldwide Application Security Project | Nonprofit behind the OWASP Top 10 web-security resources. |

## Governance, risk & compliance

Maps mainly to **Domain 5 (Security Program Management and Oversight, 20%)**. Overlaps the [WALLIX compliance map](../../reference/compliance-and-standards.md) and [CEH governance table](../../ceh/reference/acronyms.md#governance--standards).

| Acronym | Expansion | Context |
| --- | --- | --- |
| GRC | Governance, Risk, and Compliance | Discipline aligning security with business risk and regulation. |
| CIA | Confidentiality, Integrity, Availability | The "CIA triad" — three core goals of information security. |
| AAA | Authentication, Authorization, Accounting | (Also a GRC accountability concept — see access table.) |
| GDPR | General Data Protection Regulation | EU regulation governing personal-data protection and privacy. |
| HIPAA | Health Insurance Portability and Accountability Act | US law protecting health information. |
| PCI DSS | Payment Card Industry Data Security Standard | Security requirements for handling payment-card data. |
| SOX | Sarbanes–Oxley Act | US law with controls relevant to financial-reporting integrity. |
| SOC 2 | System and Organization Controls 2 | AICPA report on a service org's security/availability/confidentiality controls. |
| ISO | International Organization for Standardization | Issues standards such as ISO/IEC 27001 (ISMS) and 27002 (controls). |
| NIST | National Institute of Standards and Technology | US agency publishing security frameworks (CSF, RMF, SP 800 series). |
| CSF | Cybersecurity Framework | NIST's voluntary framework (Identify, Protect, Detect, Respond, Recover, Govern). |
| RMF | Risk Management Framework | NIST SP 800-37 process for managing system risk through the lifecycle. |
| BIA | Business Impact Analysis | Identifies critical functions and the impact of their disruption (sets RTO/RPO). |
| RTO | Recovery Time Objective | Maximum tolerable time to restore a function after disruption. |
| RPO | Recovery Point Objective | Maximum tolerable data loss, measured as time since the last good backup. |
| MTTR | Mean Time To Repair | Average time to repair a failed component (a maintainability metric). |
| MTBF | Mean Time Between Failures | Average operating time between failures of a repairable system. |
| MTTF | Mean Time To Failure | Average lifespan of a **non-repairable** component before it fails. |
| SLE | Single Loss Expectancy | Expected monetary loss from one occurrence of a risk (Asset Value × EF). |
| EF | Exposure Factor | Fraction of an asset's value lost in a single event (used in SLE). |
| ALE | Annualized Loss Expectancy | Expected yearly loss from a risk (SLE × ARO). |
| ARO | Annualized Rate of Occurrence | Expected number of times a risk occurs per year. |
| SLA | Service Level Agreement | Contract defining the service level (e.g. uptime) a provider must meet. |
| MOU | Memorandum of Understanding | Non-binding statement of intent between parties. |
| MOA | Memorandum of Agreement | More formal agreement of responsibilities than an MOU. |
| MSA | Master Service Agreement | Umbrella contract setting terms for future work/orders. |
| SOW | Statement of Work | Document detailing deliverables, timeline and scope for an engagement. |
| NDA | Non-Disclosure Agreement | Contract obliging parties to keep shared information confidential. |
| BPA | Business Partners Agreement | Agreement defining the terms of a business partnership. |
| ISA | Interconnection Security Agreement | Agreement governing the security of a connection between two organisations' systems. |
| AUP | Acceptable Use Policy | Policy defining permitted use of organisational systems. |
| KRI | Key Risk Indicator | Metric signalling rising risk exposure (leading indicator). |
| KPI | Key Performance Indicator | Metric measuring performance against an objective. |
| MSP / MSSP | Managed Service Provider / Managed Security Service Provider | Outsourced IT / outsourced security operations provider. |
| DPO | Data Protection Officer | Role accountable for data-protection compliance (e.g. under GDPR). |

## Cloud & virtualization

Maps to **Domain 3 (Security Architecture)**. Overlaps the [CEH cloud table](../../ceh/reference/acronyms.md#cloud-iot--ot).

| Acronym | Expansion | Context |
| --- | --- | --- |
| IaaS | Infrastructure as a Service | Cloud model providing raw compute/storage/network; customer secures the OS up. |
| PaaS | Platform as a Service | Managed application platform; provider secures more of the stack. |
| SaaS | Software as a Service | Finished applications; provider secures most layers. |
| CASB | Cloud Access Security Broker | Control point enforcing security policy between users and cloud services. |
| CSPM | Cloud Security Posture Management | Tooling that finds and fixes cloud misconfigurations and compliance drift. |
| CWPP | Cloud Workload Protection Platform | Security tooling protecting cloud workloads (VMs, containers). |
| CIEM | Cloud Infrastructure Entitlement Management | Right-sizes and governs identities' entitlements in the cloud. |
| VM | Virtual Machine | Software-emulated computer running on a hypervisor. |
| VDI | Virtual Desktop Infrastructure | Hosting desktop environments centrally and streaming them to clients. |
| IaC | Infrastructure as Code | Provisioning/configuring infrastructure from version-controlled definitions. |
| CI/CD | Continuous Integration / Continuous Delivery (or Deployment) | Automated build/test/release pipeline; a software-supply-chain control point. |
| SBOM | Software Bill of Materials | Inventory of components in software, used for supply-chain risk and patching. |
| SWG | Secure Web Gateway | Proxy filtering outbound web traffic against policy and threats. |
| FWaaS | Firewall as a Service | Cloud-delivered firewall capability (part of SASE). |
| API | Application Programming Interface | Key integration surface in cloud architectures (see web table). |

## Wireless & mobile

Maps to **Domain 3** and **Domain 4**. Overlaps the [CEH](../../ceh/reference/acronyms.md) list.

| Acronym | Expansion | Context |
| --- | --- | --- |
| WPA2 | Wi-Fi Protected Access 2 | Wi-Fi security using AES-CCMP; superseded by WPA3. |
| WPA3 | Wi-Fi Protected Access 3 | Current Wi-Fi security adding SAE and stronger protections. |
| WEP | Wired Equivalent Privacy | Obsolete, broken Wi-Fi encryption (RC4-based). |
| WPS | Wi-Fi Protected Setup | Simplified Wi-Fi pairing; vulnerable to PIN brute force. |
| MDM | Mobile Device Management | Centralised policy/enforcement for mobile devices. |
| UEM | Unified Endpoint Management | Single platform managing mobile, desktop and IoT endpoints. |
| BYOD | Bring Your Own Device | Employees use personal devices for work (deployment model). |
| COPE | Corporate-Owned, Personally Enabled | Company device that allows limited personal use. |
| CYOD | Choose Your Own Device | Employee picks from a company-approved device list. |
| EAP | Extensible Authentication Protocol | Wireless/802.1X authentication framework (see access table). |
| PSK | Pre-Shared Key | Shared password authentication (e.g. WPA2-Personal). |
| SAE | Simultaneous Authentication of Equals | WPA3 handshake (Dragonfly) replacing WPA2's PSK 4-way handshake. |
| AP | Access Point | Device bridging wireless clients to a wired network; rogue APs are a threat. |
| SSID | Service Set Identifier | The broadcast name of a Wi-Fi network. |
| RFID | Radio-Frequency Identification | Wireless tag/reader technology; cloning is a physical-access threat. |
| NFC | Near-Field Communication | Very-short-range wireless used for payments/access; relay attacks are a risk. |
| GPS | Global Positioning System | Location service; spoofing/jamming are availability/integrity threats. |

## Physical, IoT & OT

Maps to **Domain 3** (architecture) and **Domain 2** (threats). Overlaps the [CEH IoT/OT table](../../ceh/reference/acronyms.md#cloud-iot--ot).

| Acronym | Expansion | Context |
| --- | --- | --- |
| ICS | Industrial Control System | Umbrella term for systems controlling industrial processes. |
| SCADA | Supervisory Control and Data Acquisition | Systems supervising and gathering data from distributed industrial processes. |
| PLC | Programmable Logic Controller | Ruggedised industrial computer controlling machinery within an ICS. |
| HMI | Human-Machine Interface | Operator console used to interact with an ICS/SCADA system. |
| RTOS | Real-Time Operating System | OS guaranteeing timing for embedded/control systems. |
| HVAC | Heating, Ventilation, and Air Conditioning | Building system; an OT attack surface and an availability dependency. |
| UPS | Uninterruptible Power Supply | Battery backup keeping equipment running through power loss (availability). |
| PDU | Power Distribution Unit | Rack device distributing power to equipment. |
| IoT | Internet of Things | Networked everyday/embedded devices; often weakly secured. |
| SoC | System on a Chip | Integrated circuit packing a whole system; common in embedded/IoT devices. |
| RFID | Radio-Frequency Identification | Tag-based identification used in badges/inventory (see wireless table). |
| CCTV | Closed-Circuit Television | Camera-based physical surveillance/monitoring. |
| OT | Operational Technology | Hardware/software monitoring and controlling physical processes (contrast IT). |
| BAS | Building Automation System | Networked control of building services (HVAC, lighting, access). |

## Incident response, forensics & resilience

Maps to **Domain 4** (incident response) and **Domain 5** (resilience/continuity).

| Acronym | Expansion | Context |
| --- | --- | --- |
| IR | Incident Response | The organised process for handling a security incident. |
| IRP | Incident Response Plan | The documented plan governing IR. |
| CSIRT | Computer Security Incident Response Team | The team that executes incident response. |
| CIRT / CERT | Computer Incident Response Team / Computer Emergency Response Team | Synonyms for the IR team (CERT is also a registered name for specific bodies). |
| SOC | Security Operations Center | Continuous monitoring/response team (see operations table). |
| BCP | Business Continuity Plan | Plan to keep critical business functions running during disruption. |
| DRP | Disaster Recovery Plan | Plan to restore IT systems and data after a disaster. |
| COOP | Continuity of Operations | Government/organisational program ensuring essential functions continue. |
| RCA | Root Cause Analysis | Post-incident analysis identifying the underlying cause to prevent recurrence. |
| CoC | Chain of Custody | Documented handling of evidence preserving its integrity for legal use. |
| IoC | Indicator of Compromise | Evidence a system may be breached (see operations table). |
| MTTR / RTO / RPO | (see GRC table) | Recovery metrics central to continuity planning. |
| AAR | After-Action Report | Post-exercise/post-incident review of what happened and lessons learned. |
| HA | High Availability | Designing to avoid single points of failure (uptime). |
| DR | Disaster Recovery | Restoring service after a major outage. |

## Attacks, vulnerabilities & threats

Maps mainly to **Domain 2 (Threats, Vulnerabilities, and Mitigations, 22%)**. Offensive items are framed defensively; see the [CEH attack table](../../ceh/reference/acronyms.md#attack--security-concepts) for depth.

| Acronym | Expansion | Context |
| --- | --- | --- |
| APT | Advanced Persistent Threat | Well-resourced, stealthy adversary maintaining long-term access. |
| DoS | Denial of Service | Making a service unavailable by exhausting its resources. |
| DDoS | Distributed Denial of Service | A DoS from many sources at once (often a botnet). |
| MITM / OTW | Man-in-the-Middle / On-Path attack | Attacker secretly relays/alters traffic between two parties (CompTIA prefers "on-path"). |
| RAT | Remote Access Trojan | Malware giving an attacker remote control of a host. |
| C2 | Command and Control | Infrastructure an attacker uses to direct compromised hosts. |
| RCE | Remote Code Execution | Vulnerability letting an attacker run arbitrary code on a remote system. |
| PtH / PtT | Pass-the-Hash / Pass-the-Ticket | Reusing a stolen hash/Kerberos ticket to authenticate without the password. |
| BEC | Business Email Compromise | Social-engineering fraud impersonating a trusted party over email. |
| PII | Personally Identifiable Information | Data that can identify an individual; a protection and breach-impact concept. |
| PHI | Protected Health Information | Health data protected under regulations such as HIPAA. |
| IP (theft) | Intellectual Property | Proprietary assets (designs, code, trade secrets) targeted by espionage. |
| TOC/TOU | Time-of-Check to Time-of-Use | Race-condition flaw where state changes between validation and use. |
| DDoS / DoS | (see above) | Availability attacks within Domain 2. |
| EOL / EOSL | End of Life / End of Service Life | Unsupported software/hardware that no longer receives patches — a vulnerability. |
| 0-day / zero-day | (not an acronym) | A vulnerability exploited before a patch exists. |
| BIA | Business Impact Analysis | (Risk side; see GRC table.) |

## See also

- [glossary.md](glossary.md) — prose definitions of Security+ terms, cross-linked to the domain pages.
- [General Security Concepts (Domain 1)](../domains/01-general-security-concepts.md)
- [Threats, Vulnerabilities, and Mitigations (Domain 2)](../domains/02-threats-vulnerabilities-mitigations.md)
- [Security Architecture (Domain 3)](../domains/03-security-architecture.md)
- [Security Operations (Domain 4)](../domains/04-security-operations.md)
- [Security Program Management and Oversight (Domain 5)](../domains/05-security-program-management-oversight.md)
- [Exam format and objectives](../00-overview/exam-and-objectives.md) — where to download CompTIA's official acronym appendix.
- [WALLIX acronyms](../../reference/acronyms.md) · [CEH acronyms](../../ceh/reference/acronyms.md) — the repo's sibling lists.

## Sources

- CompTIA — Security+ certification page and official **SY0-701 exam objectives** PDF (which contains the authoritative acronym appendix): https://www.comptia.org/en-us/certifications/security/ *(download and verify; the acronym list is the appendix at the end of the objectives)*
- NIST Computer Security Resource Center — Glossary (term/acronym definitions): https://csrc.nist.gov/glossary
- NIST FIPS 197 (AES): https://csrc.nist.gov/pubs/fips/197/final ; FIPS 180-4 (SHA): https://csrc.nist.gov/pubs/fips/180-4/upd1/final ; FIPS 198-1 (HMAC): https://csrc.nist.gov/pubs/fips/198-1/final
- NIST SP 800-37 (RMF): https://csrc.nist.gov/pubs/sp/800/37/r2/final ; NIST Cybersecurity Framework (CSF) 2.0: https://www.nist.gov/cyberframework
- IETF RFCs for protocols referenced (e.g. TLS 1.3 — RFC 8446; OAuth 2.0 — RFC 6749; OpenID Connect Core; SAML 2.0 OASIS standard; RADIUS — RFC 2865): https://www.rfc-editor.org/
- IANA Service Name and Transport Protocol Port Number Registry (default ports — confirm in practice; services can be reconfigured): https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml
- FIDO Alliance — https://fidoalliance.org/ ; OWASP — https://owasp.org/ ; MITRE ATT&CK — https://attack.mitre.org/
