# CEH Acronyms Reference

> 🔁 This is the **CEH / offensive** acronym list. For PAM, identity & WALLIX acronyms, see the [WALLIX acronyms reference](../../reference/acronyms.md).

A comprehensive, categorised reference of acronyms and initialisms you will meet across the Certified Ethical Hacker (CEH) curriculum and this study hub. Each table gives the **acronym**, its **expansion**, and a **one-line context** to anchor it in CEH terms. Acronyms are expanded on first use throughout the hub; this page is the master list.

Where a term is offensive, it is described **neutrally with a defensive framing** — the point of CEH is to understand attacks so you can defend against them. For broader prose definitions, see the [glossary](./glossary.md).

> Tip for a sysadmin: skim the **Protocols & ports** and **Defense & operations** tables first — much of that vocabulary you already know from administration; CEH reframes it from the attacker's viewpoint.

## Contents

- [Certification & exam](#certification--exam)
- [Attack & security concepts](#attack--security-concepts)
- [Defense & operations](#defense--operations)
- [Protocols & ports](#protocols--ports)
- [Web & application](#web--application)
- [Cryptography](#cryptography)
- [Cloud, IoT & OT](#cloud-iot--ot)
- [Governance & standards](#governance--standards)

## Certification & exam

| Acronym | Expansion | Context |
| --- | --- | --- |
| CEH | Certified Ethical Hacker | The vendor-neutral certification this hub is built around; see [what-is-ceh.md](../00-overview/what-is-ceh.md). |
| C\|EH | Certified Ethical Hacker | EC-Council's own stylised branding of the CEH mark (the pipe is decorative). |
| EC-Council | International Council of E-Commerce Consultants | The certification body that creates and issues CEH; see [exam-and-eligibility.md](../00-overview/exam-and-eligibility.md). |
| ATC | Accredited Training Center | An EC-Council-authorised partner that delivers official CEH training and exam eligibility. |
| ECE | EC-Council Continuing Education | The credit scheme used to keep a CEH valid after issue (credits over the validity period; verify totals on EC-Council). |
| ANSI | American National Standards Institute | Standards body historically associated with accrediting CEH under ISO/IEC 17024. |
| MCQ | Multiple-Choice Question | The question format of the CEH knowledge exam (312-50). |
| CTF | Capture The Flag | Gamified challenges (the "Compete" pillar) where you capture hidden tokens by solving security puzzles. |
| RoE | Rules of Engagement | The agreed scope, limits, and authorisation governing an ethical-hacking engagement. |
| CPE | Continuing Professional Education | Generic term for ongoing-education credits used by many certification bodies (compare ECE). |

## Attack & security concepts

| Acronym | Expansion | Context |
| --- | --- | --- |
| APT | Advanced Persistent Threat | A well-resourced, stealthy adversary that maintains long-term access; the model behind much of CEH's methodology. |
| C2 | Command and Control | Infrastructure an attacker uses to remotely instruct compromised hosts; detecting C2 traffic is a core defensive skill. |
| CSRF | Cross-Site Request Forgery | A web attack that tricks a logged-in user's browser into sending unwanted authenticated requests. |
| DoS | Denial of Service | An attack that makes a service unavailable by exhausting its resources; covered in the Denial-of-Service module. |
| DDoS | Distributed Denial of Service | A DoS launched from many sources at once (often a botnet), making it harder to block. |
| IDOR | Insecure Direct Object Reference | An access-control flaw where changing a reference (e.g., an ID in a URL) exposes another user's data. |
| IOC | Indicator of Compromise | Forensic evidence (hashes, IPs, domains, artifacts) that a system may have been breached. |
| LFI | Local File Inclusion | A web flaw that lets an attacker include files already on the server, often leading to information disclosure or code execution. |
| MITM | Man-in-the-Middle | An attacker secretly relays/alters traffic between two parties; the focus of the Sniffing module. |
| PtH | Pass-the-Hash | Authenticating with a captured password **hash** instead of the plaintext password (common in Windows/Active Directory attacks). |
| PtT | Pass-the-Ticket | Reusing a stolen Kerberos **ticket** to authenticate without the password. |
| RAT | Remote Access Trojan | Malware giving an attacker remote control of a host; covered under Malware Threats. |
| RCE | Remote Code Execution | A vulnerability class that lets an attacker run arbitrary code on a remote system — among the most severe outcomes. |
| RFI | Remote File Inclusion | A web flaw that lets an attacker include a **remote** file, often executing attacker-hosted code. |
| SSRF | Server-Side Request Forgery | Tricking a server into making requests on the attacker's behalf, often to reach internal services. |
| TTP | Tactics, Techniques, and Procedures | The behavioural "fingerprint" of an adversary; mapped in frameworks like MITRE ATT&CK. |
| XSS | Cross-Site Scripting | Injecting attacker-controlled script into pages other users view; a core web-application attack. |
| OSINT | Open-Source Intelligence | Intelligence gathered from publicly available sources during reconnaissance/footprinting. |
| PoC | Proof of Concept | A minimal demonstration that a vulnerability is exploitable, without full weaponisation. |
| BEC | Business Email Compromise | A social-engineering fraud where an attacker impersonates a trusted party over email. |

## Defense & operations

| Acronym | Expansion | Context |
| --- | --- | --- |
| DLP | Data Loss Prevention | Controls that detect and block sensitive data leaving an organisation. |
| DMZ | Demilitarised Zone | A buffer network segment between the internet and the internal network for public-facing services. |
| EDR | Endpoint Detection and Response | Agent-based tooling that monitors endpoints for malicious behaviour and enables response. |
| IDS | Intrusion Detection System | Monitors traffic/hosts and **alerts** on suspicious activity; evading IDS is its own CEH module. |
| IPS | Intrusion Prevention System | Like an IDS but can **block** detected threats inline. |
| MFA | Multi-Factor Authentication | Requiring two or more authentication factors; a key control against credential attacks. |
| NAC | Network Access Control | Enforces policy on which devices may join a network and under what conditions. |
| PKI | Public Key Infrastructure | The framework of keys, certificates, and authorities that underpins TLS, code signing, and more. |
| SIEM | Security Information and Event Management | Aggregates and correlates logs/events for detection and investigation; central to a SOC. |
| SOC | Security Operations Center | The team/facility that monitors, detects, and responds to security events. |
| VPN | Virtual Private Network | An encrypted tunnel extending a private network over an untrusted one. |
| WAF | Web Application Firewall | Filters and monitors HTTP(S) traffic to protect web apps from attacks like SQLi and XSS. |
| XDR | Extended Detection and Response | Correlates detection/response across endpoints, network, identity, and cloud (an evolution of EDR). |
| SOAR | Security Orchestration, Automation, and Response | Automates and coordinates SOC workflows and playbooks. |
| HIDS | Host-based Intrusion Detection System | An IDS that runs on and watches a single host. |
| NIDS | Network-based Intrusion Detection System | An IDS that inspects network traffic on a segment. |
| UTM | Unified Threat Management | A single appliance combining firewall, IPS, antivirus, and other controls. |

## Protocols & ports

Default ports are the common assignments; services can be reconfigured, so always confirm during scanning/enumeration.

| Acronym | Expansion | Context (default port) |
| --- | --- | --- |
| ARP | Address Resolution Protocol | Maps IP addresses to MAC addresses on a LAN; the target of ARP spoofing/poisoning (no port — Layer 2). |
| DHCP | Dynamic Host Configuration Protocol | Assigns IP addresses automatically; can be abused via rogue DHCP servers (UDP 67/68). |
| DNS | Domain Name System | Resolves names to IP addresses; a frequent recon target and exfiltration channel (UDP/TCP 53). |
| FTP | File Transfer Protocol | Cleartext file transfer; credentials are sniffable (TCP 20/21). |
| HTTP | HyperText Transfer Protocol | The unencrypted web protocol (TCP 80). |
| HTTPS | HyperText Transfer Protocol Secure | HTTP wrapped in TLS for confidentiality/integrity (TCP 443). |
| ICMP | Internet Control Message Protocol | Diagnostics/error messaging (e.g., ping); used in host discovery and some tunnelling (no port — Layer 3). |
| LDAP | Lightweight Directory Access Protocol | Queries directory services such as Active Directory; key to enumeration (TCP/UDP 389; LDAPS 636). |
| RDP | Remote Desktop Protocol | Windows remote graphical access; a common brute-force/lateral-movement target (TCP 3389). |
| SMB | Server Message Block | Windows file/printer sharing; central to many Windows attacks (TCP 445). |
| SMTP | Simple Mail Transfer Protocol | Sends email; abused for relay and user enumeration (TCP 25; also 587/465). |
| SNMP | Simple Network Management Protocol | Manages/monitors network devices; weak community strings leak data (UDP 161/162). |
| SSH | Secure Shell | Encrypted remote shell and tunnelling; brute-force and key-theft target (TCP 22). |
| TCP | Transmission Control Protocol | Connection-oriented, reliable transport; basis of most port scanning (no fixed port — Layer 4). |
| UDP | User Datagram Protocol | Connectionless, lightweight transport; used by DNS, DHCP, SNMP (no fixed port — Layer 4). |
| SSL | Secure Sockets Layer | The deprecated predecessor to TLS; still loosely used to mean "the encryption layer." |
| TLS | Transport Layer Security | The modern protocol that encrypts HTTPS and many other services. |
| NTP | Network Time Protocol | Time synchronisation; abused in DDoS amplification (UDP 123). |
| TFTP | Trivial File Transfer Protocol | Minimal, unauthenticated file transfer (UDP 69). |
| Telnet | Telnet (not an acronym) | Legacy cleartext remote shell; credentials sniffable (TCP 23). |

## Web & application

| Acronym | Expansion | Context |
| --- | --- | --- |
| API | Application Programming Interface | The contract through which software components talk; a growing attack surface. |
| CORS | Cross-Origin Resource Sharing | Browser mechanism that relaxes the Same-Origin Policy; misconfiguration can leak data. |
| JWT | JSON Web Token | A signed token format for authentication/authorisation; weak signing/validation is exploitable. |
| OWASP | Open Worldwide Application Security Project | Nonprofit behind the OWASP Top 10 and many web-security resources. |
| SOP | Same-Origin Policy | The browser rule isolating content by origin (scheme + host + port); the baseline CORS relaxes. |
| SQLi | SQL Injection | Injecting attacker-controlled SQL into a query; its own CEH module (Module 15). |
| JSON | JavaScript Object Notation | Lightweight data-interchange format common in APIs and tokens (JWT). |
| XML | eXtensible Markup Language | Markup data format; related to attacks such as XXE (XML External Entity). |
| XXE | XML External Entity | An attack abusing XML parsers to read files or reach internal systems. |
| CMS | Content Management System | Web platform (e.g., for sites/blogs) often targeted via plugins/misconfiguration. |
| WSDL | Web Services Description Language | XML description of a web service's interface; useful during web-service enumeration. |

## Cryptography

| Acronym | Expansion | Context |
| --- | --- | --- |
| AES | Advanced Encryption Standard | The dominant symmetric block cipher (128/192/256-bit keys). |
| DES | Data Encryption Standard | A legacy symmetric cipher, now insecure due to its 56-bit key. |
| 3DES | Triple Data Encryption Standard | Runs DES three times to extend key strength; now deprecated. |
| ECC | Elliptic Curve Cryptography | Public-key cryptography giving strong security with smaller keys. |
| FIDO | Fast IDentity Online | Standards (e.g., FIDO2/WebAuthn) for phishing-resistant, passwordless authentication. |
| HMAC | Hash-based Message Authentication Code | Combines a hash with a secret key to verify integrity **and** authenticity. |
| MD5 | Message Digest 5 | A legacy 128-bit hash, broken for collision resistance; still seen for non-security checksums. |
| RSA | Rivest–Shamir–Adleman | A widely used public-key algorithm for encryption and digital signatures. |
| SHA | Secure Hash Algorithm | A family of hash functions (SHA-1 deprecated; SHA-2/SHA-3 current). |
| TOTP | Time-based One-Time Password | A time-synced one-time code (e.g., authenticator apps) used as a second factor. |
| HOTP | HMAC-based One-Time Password | A counter-based one-time-password scheme (the basis TOTP builds on). |
| PGP | Pretty Good Privacy | Software/standard for encrypting and signing data and email. |
| CA | Certificate Authority | A trusted issuer of digital certificates within a PKI. |
| CSR | Certificate Signing Request | A request submitted to a CA to obtain a signed certificate. |

## Cloud, IoT & OT

| Acronym | Expansion | Context |
| --- | --- | --- |
| IaaS | Infrastructure as a Service | Cloud model providing raw compute/storage/network; customer secures the OS and up. |
| PaaS | Platform as a Service | Cloud model providing a managed application platform; provider secures more of the stack. |
| SaaS | Software as a Service | Cloud model delivering finished applications; provider secures most layers. |
| CASB | Cloud Access Security Broker | A control point enforcing security policy between users and cloud services. |
| CSPM | Cloud Security Posture Management | Tooling that finds and fixes cloud misconfigurations and compliance drift. |
| ICS | Industrial Control System | Umbrella term for systems controlling industrial processes; a CEH OT topic. |
| IoT | Internet of Things | Networked everyday/embedded devices; their own hacking module (Module 18). |
| OT | Operational Technology | Hardware/software that monitors and controls physical processes (contrast with IT). |
| PLC | Programmable Logic Controller | A ruggedised industrial computer that controls machinery within an ICS. |
| SCADA | Supervisory Control and Data Acquisition | Systems that supervise and gather data from distributed industrial processes. |
| HMI | Human-Machine Interface | The operator screen/console used to interact with an ICS/SCADA system. |
| RTU | Remote Terminal Unit | A field device that relays sensor/control data to a SCADA master. |
| CWPP | Cloud Workload Protection Platform | Security tooling focused on protecting cloud workloads (VMs, containers). |

## Governance & standards

| Acronym | Expansion | Context |
| --- | --- | --- |
| CIA | Confidentiality, Integrity, Availability | The "CIA triad" — the three core goals of information security. |
| CVE | Common Vulnerabilities and Exposures | A public catalogue assigning unique IDs to known vulnerabilities. |
| CVSS | Common Vulnerability Scoring System | A standard 0–10 severity score for vulnerabilities. |
| CWE | Common Weakness Enumeration | A catalogue of software/hardware **weakness types** (the root causes behind CVEs). |
| GDPR | General Data Protection Regulation | The European Union regulation governing personal-data protection and privacy. |
| HIPAA | Health Insurance Portability and Accountability Act | US law setting protections for health information. |
| ISO 27001 | ISO/IEC 27001 | The international standard for an Information Security Management System (ISMS). |
| NIST | National Institute of Standards and Technology | US agency publishing widely used security standards/frameworks (e.g., the Cybersecurity Framework, SP 800 series). |
| PCI DSS | Payment Card Industry Data Security Standard | Security requirements for organisations handling payment-card data. |
| GRC | Governance, Risk, and Compliance | The discipline aligning security with business risk and regulation. |
| ISMS | Information Security Management System | The managed set of policies/processes formalised by ISO 27001. |
| SOX | Sarbanes–Oxley Act | US law with controls relevant to financial-reporting data integrity. |
| ATT&CK | Adversarial Tactics, Techniques, and Common Knowledge | MITRE's knowledge base of real-world adversary TTPs. |
| CISA | Cybersecurity and Infrastructure Security Agency | US agency for national cyber defence (note: also a separate ISACA certification — context matters). |

## Where to go next

- [glossary.md](./glossary.md) — prose definitions of CEH terms, cross-linked to the modules.
- [what-is-ceh.md](../00-overview/what-is-ceh.md) — what CEH is and who issues it.
- [exam-and-eligibility.md](../00-overview/exam-and-eligibility.md) — exam format, eligibility, and accreditations.
- [../career/ceh-career-and-adjacent-certs.md](../career/ceh-career-and-adjacent-certs.md) — where CEH fits in a career.

## Sources

- EC-Council, Certified Ethical Hacker (CEH) v13 program and learning framework — https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/ and https://www.eccouncil.org/cybersecurity-exchange/ethical-hacking/ceh-learning-framework/
- OWASP (Open Worldwide Application Security Project) — https://owasp.org/
- MITRE ATT&CK knowledge base — https://attack.mitre.org/
- MITRE CVE program — https://www.cve.org/ ; CWE — https://cwe.mitre.org/
- FIRST, Common Vulnerability Scoring System (CVSS) — https://www.first.org/cvss/
- NIST (National Institute of Standards and Technology) — https://www.nist.gov/
- ISO/IEC 27001 — https://www.iso.org/standard/27001
- FIDO Alliance — https://fidoalliance.org/
- Default port assignments per IANA Service Name and Transport Protocol Port Number Registry — https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml (confirm in practice; services can be reconfigured)
