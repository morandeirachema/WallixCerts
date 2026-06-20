# Security+ (SY0-701) Practice Questions (Unofficial)

A bank of **50+ multiple-choice practice questions** grouped by the five CompTIA Security+ (SY0-701) domains, each with the correct answer and a short explanation that links to the relevant page in this hub. They are study aids built around standard, documented Security+ concepts.

> **Unofficial practice questions — NOT real CompTIA exam questions.** These are pedagogical study aids written for this hub to rehearse documented Security+ concepts. They are not drawn from, affiliated with, or endorsed by CompTIA, and they do not reproduce any actual exam item. The real exam is **a maximum of 90 questions (multiple-choice + performance-based) in 90 minutes**; passing is **750 on a 100–900 scaled score** — *verify on CompTIA*.

## How to use these

1. **Cover the answers.** Read the question, commit to an option, *then* reveal the answer line.
2. **Read the explanation even when you are right** — the reasoning is the point, not the letter.
3. **Track misses by domain.** If you miss two or more in a domain, re-read that [domain page](../domains/README.md) before moving on.
4. **Simulate pressure.** In your final week, answer in timed blocks (the real exam averages ~1 minute per item).
5. **Pair with the** [study-plan.md](./study-plan.md) **schedule and the** [cheat-sheet.md](./cheat-sheet.md) **for the facts these lean on.**

> **Acronyms** are expanded on first use. A consolidated list lives in [../reference/acronyms.md](../reference/acronyms.md).

---

## Domain 1 — General Security Concepts (12%)

**Q1.** Which trio defines the core goals of information security?
- A. Authentication, Authorisation, Accounting
- B. Confidentiality, Integrity, Availability
- C. Prevention, Detection, Response
- D. People, Process, Technology

**Answer: B.** The **CIA triad** — Confidentiality, Integrity, Availability — is the foundational model. AAA (option A) is the access framework, not the triad. See [Domain 1](../domains/01-general-security-concepts.md).

**Q2.** A locked server-room door is an example of which control category?
- A. Technical
- B. Managerial
- C. Physical
- D. Operational

**Answer: C.** A physical lock is a **physical** control. Technical controls are technological (firewalls, encryption); managerial are policy/risk decisions; operational are people-driven processes. See [Domain 1](../domains/01-general-security-concepts.md).

**Q3.** A security camera that records who enters a room is primarily which **control type**?
- A. Preventive
- B. Detective
- C. Corrective
- D. Compensating

**Answer: B.** A camera **detects/records** activity rather than stopping it, so it is **detective**. A lock would be preventive; a backup restore is corrective. See [Domain 1](../domains/01-general-security-concepts.md).

**Q4.** Under **Zero Trust**, network location is treated how?
- A. Internal traffic is automatically trusted
- B. No user or device is trusted by default; every request is verified
- C. Only the perimeter firewall enforces trust
- D. VPN users are exempt from verification

**Answer: B.** Zero Trust assumes **no implicit trust** — "never trust, always verify" — regardless of location. See [Domain 1](../domains/01-general-security-concepts.md) and [../../foundations/core-concepts-least-privilege-jit-zero-trust.md](../../foundations/core-concepts-least-privilege-jit-zero-trust.md).

**Q5.** In **AAA**, which element answers "what is this authenticated user allowed to do?"
- A. Authentication
- B. Authorisation
- C. Accounting
- D. Auditing

**Answer: B.** **Authorisation** determines permitted actions after **authentication** proves identity; **accounting** logs what was done. See [Domain 1](../domains/01-general-security-concepts.md).

**Q6.** A formal process to request, review, approve, and document modifications to systems is:
- A. Incident response
- B. Change management
- C. Vulnerability scanning
- D. Risk transfer

**Answer: B.** **Change management** governs how changes are proposed, assessed, approved, and recorded to avoid uncontrolled, risky changes. See [Domain 1](../domains/01-general-security-concepts.md).

---

## Domain 2 — Threats, Vulnerabilities, and Mitigations (22%)

**Q7.** A targeted phishing email crafted for one senior executive (a CEO) is best called:
- A. Spear phishing
- B. Whaling
- C. Vishing
- D. Smishing

**Answer: B.** **Whaling** targets high-value executives ("big fish"). Spear phishing targets specific individuals generally; vishing is voice, smishing is SMS. See [Domain 2](../domains/02-threats-vulnerabilities-mitigations.md).

**Q8.** Malware that encrypts a victim's files and demands payment for the key is:
- A. A rootkit
- B. Ransomware
- C. Spyware
- D. A logic bomb

**Answer: B.** **Ransomware** encrypts data and extorts payment. Tested mitigations are tested, offline **backups** and user awareness. See [Domain 2](../domains/02-threats-vulnerabilities-mitigations.md).

**Q9.** A threat actor motivated by ideology or a political/social cause is best classified as a(n):
- A. Nation-state actor
- B. Hacktivist
- C. Organised-crime group
- D. Script kiddie

**Answer: B.** A **hacktivist** is driven by ideology rather than profit (organised crime) or espionage (nation-state). See [Domain 2](../domains/02-threats-vulnerabilities-mitigations.md).

**Q10.** The single most effective defence against SQL injection is:
- A. Hiding the database version
- B. Using parameterised queries (prepared statements)
- C. Renaming tables
- D. Disabling cookies

**Answer: B.** **Parameterised queries** separate code from data so input cannot be executed as SQL. Input validation and least privilege are supporting controls. See [Domain 2](../domains/02-threats-vulnerabilities-mitigations.md).

**Q11.** An attack exploiting a flaw that the vendor does not yet know about and has no patch for is a:
- A. Zero-day attack
- B. Brute-force attack
- C. Replay attack
- D. Downgrade attack

**Answer: A.** A **zero-day** targets an unknown, unpatched vulnerability — defenders have had "zero days" to fix it. See [Domain 2](../domains/02-threats-vulnerabilities-mitigations.md).

**Q12.** An employee with legitimate access who deliberately steals data is an example of a(n):
- A. Insider threat
- B. Advanced persistent threat
- C. Supply-chain attack
- D. Watering-hole attack

**Answer: A.** An **insider threat** misuses authorised access. Least privilege, separation of duties, and monitoring reduce the impact. See [Domain 2](../domains/02-threats-vulnerabilities-mitigations.md).

**Q13.** Plugging an unknown found USB drive into a work computer most directly risks:
- A. A volumetric DDoS
- B. Malware execution from a "baiting" attack
- C. An ARP-poisoning attack
- D. A certificate-pinning failure

**Answer: B.** Dropping malicious USB media is **baiting** social engineering; disabling autorun and blocking unknown USB devices mitigates it. See [Domain 2](../domains/02-threats-vulnerabilities-mitigations.md).

**Q14.** Tricking users by registering a domain that looks almost identical to a real one (e.g., a swapped letter) is:
- A. Pharming
- B. Typosquatting
- C. Pretexting
- D. Tailgating

**Answer: B.** **Typosquatting** (URL hijacking) relies on misspelled look-alike domains to harvest credentials or deliver malware. See [Domain 2](../domains/02-threats-vulnerabilities-mitigations.md).

---

## Domain 3 — Security Architecture (18%)

**Q15.** In the cloud **shared-responsibility model** for Infrastructure as a Service (IaaS), the customer is generally responsible for:
- A. The physical data centre
- B. The hypervisor
- C. The guest operating system, applications, and data
- D. The underlying network hardware

**Answer: C.** Under IaaS the provider secures the physical and virtualisation layers; the **customer** secures the OS, apps, and data. See [Domain 3](../domains/03-security-architecture.md).

**Q16.** Dividing a network into isolated zones to limit how far an attacker can move is:
- A. Network segmentation
- B. Port forwarding
- C. Load balancing
- D. NAT

**Answer: A.** **Segmentation** restricts lateral movement and contains breaches. A demilitarised zone (DMZ) and VLANs are common implementations. See [Domain 3](../domains/03-security-architecture.md).

**Q17.** Protecting data **in transit** between a browser and a web server is the job of:
- A. Full-disk encryption
- B. Transport Layer Security (TLS)
- C. A hashing algorithm
- D. Tokenisation

**Answer: B.** **TLS** encrypts data in transit. Full-disk encryption protects data **at rest**; hashing provides integrity, not confidentiality. See [Domain 3](../domains/03-security-architecture.md).

**Q18.** Two servers behind a load balancer so that if one fails the service stays up is an example of:
- A. Confidentiality
- B. High availability
- C. Non-repudiation
- D. Steganography

**Answer: B.** Redundancy for continued operation is **high availability**, the "A" (Availability) in the CIA triad. See [Domain 3](../domains/03-security-architecture.md).

**Q19.** Replacing a credit-card number with a non-sensitive substitute value that maps back only in a secure vault is:
- A. Hashing
- B. Tokenisation
- C. Salting
- D. Obfuscation

**Answer: B.** **Tokenisation** swaps sensitive data for a meaningless token, reducing the systems in scope for protection. See [Domain 3](../domains/03-security-architecture.md).

**Q20.** A system that monitors network traffic and **actively blocks** matching malicious traffic is a(n):
- A. IDS
- B. IPS
- C. SIEM
- D. Honeypot

**Answer: B.** An **Intrusion Prevention System (IPS)** blocks inline; an **Intrusion Detection System (IDS)** only alerts. See [Domain 3](../domains/03-security-architecture.md).

**Q21.** Keeping three copies of data, on two media types, with one copy off-site, describes the:
- A. CIA triad
- B. 3-2-1 backup rule
- C. AAA model
- D. RACI matrix

**Answer: B.** The **3-2-1 rule** (3 copies, 2 media, 1 off-site) is a resilience best practice underpinning recovery. See [Domain 3](../domains/03-security-architecture.md).

---

## Domain 4 — Security Operations (28%)

**Q22.** A platform that aggregates and correlates logs from many sources to detect and alert on incidents is a:
- A. DLP
- B. SIEM
- C. CASB
- D. WAF

**Answer: B.** A **Security Information and Event Management (SIEM)** system centralises log collection, correlation, and alerting. See [Domain 4](../domains/04-security-operations.md).

**Q23.** Which is the correct order of the incident-response lifecycle?
- A. Detection → Preparation → Containment → Eradication → Recovery → Lessons Learned
- B. Preparation → Detection & Analysis → Containment → Eradication → Recovery → Lessons Learned
- C. Containment → Detection → Preparation → Recovery → Eradication → Lessons Learned
- D. Preparation → Recovery → Detection → Containment → Eradication → Lessons Learned

**Answer: B.** The standard NIST-aligned lifecycle is **Preparation → Detection & Analysis → Containment → Eradication → Recovery → Lessons Learned**. See [Domain 4](../domains/04-security-operations.md).

**Q24.** Disabling unused services, changing default passwords, and applying a secure baseline to a server is:
- A. System hardening
- B. Threat hunting
- C. Tokenisation
- D. Risk transfer

**Answer: A.** **Hardening** reduces the attack surface by removing unnecessary functionality and enforcing secure configuration. See [Domain 4](../domains/04-security-operations.md).

**Q25.** Granting users only the minimum access required for their job is the principle of:
- A. Defence in depth
- B. Least privilege
- C. Separation of duties
- D. Implicit deny

**Answer: B.** **Least privilege** limits each account to the access strictly needed, shrinking the blast radius of a compromise. See [Domain 4](../domains/04-security-operations.md) and [../../foundations/core-concepts-least-privilege-jit-zero-trust.md](../../foundations/core-concepts-least-privilege-jit-zero-trust.md).

**Q26.** Requiring a password **and** a one-time code from an authenticator app is an example of:
- A. Single sign-on
- B. Multi-factor authentication
- C. Federation
- D. Privilege escalation

**Answer: B.** **Multi-factor authentication (MFA)** combines factors from different categories (here, *something you know* + *something you have*). See [Domain 4](../domains/04-security-operations.md).

**Q27.** Which access-control model grants permissions based on a user's **job role**?
- A. Discretionary Access Control (DAC)
- B. Mandatory Access Control (MAC)
- C. Role-Based Access Control (RBAC)
- D. Rule-Based Access Control

**Answer: C.** **RBAC** assigns permissions to roles, then users to roles. MAC uses labels/clearances; DAC lets owners set access. See [Domain 4](../domains/04-security-operations.md).

**Q28.** Promptly removing all of a departing employee's accounts and access is part of:
- A. Onboarding
- B. Offboarding
- C. Change management
- D. Penetration testing

**Answer: B.** **Offboarding** deprovisions access when someone leaves — a critical control against orphaned accounts. See [Domain 4](../domains/04-security-operations.md).

**Q29.** The practice of regularly scanning systems for known weaknesses and tracking their remediation is:
- A. Vulnerability management
- B. Incident response
- C. Business continuity
- D. Data classification

**Answer: A.** **Vulnerability management** is the ongoing cycle of identifying, prioritising (often by CVSS), and remediating weaknesses. See [Domain 4](../domains/04-security-operations.md).

**Q30.** A single set of credentials that logs a user into many applications without re-entering them describes:
- A. Multi-factor authentication
- B. Single sign-on (SSO)
- C. Just-in-time access
- D. Federation only

**Answer: B.** **Single sign-on (SSO)** authenticates once for many services, improving usability; pair it with MFA for security. See [Domain 4](../domains/04-security-operations.md).

**Q31.** A tool that inspects outbound traffic and content to stop sensitive data from leaving the organisation is:
- A. Data Loss Prevention (DLP)
- B. A honeypot
- C. A jump server
- D. A SIEM

**Answer: A.** **DLP** detects and blocks unauthorised exfiltration of sensitive data (e.g., card numbers in email). See [Domain 4](../domains/04-security-operations.md).

**Q32.** The principle that no single person should control an entire critical process, reducing fraud, is:
- A. Least privilege
- B. Separation of duties
- C. Mandatory vacation
- D. Implicit deny

**Answer: B.** **Separation of duties** splits a sensitive task across people so collusion is required to abuse it. See [Domain 4](../domains/04-security-operations.md).

**Q33.** Hashing a captured disk image and re-hashing it later to prove it was not altered preserves:
- A. Chain of custody and integrity
- B. Confidentiality
- C. Availability
- D. Non-repudiation only

**Answer: A.** Matching hashes prove the evidence is unchanged, supporting **integrity** and a defensible **chain of custody** in digital forensics. See [Domain 4](../domains/04-security-operations.md).

---

## Domain 5 — Security Program Management and Oversight (20%)

**Q34.** An asset is worth $200,000 and a fire would destroy 40% of it. What is the **Single Loss Expectancy (SLE)**?
- A. $40,000
- B. $80,000
- C. $200,000
- D. $500,000

**Answer: B.** **SLE = Asset Value × Exposure Factor = 200,000 × 0.40 = $80,000.** See [Domain 5](../domains/05-security-program-management-oversight.md).

**Q35.** Using the previous question, if such a fire is expected once every 10 years (ARO = 0.1), the **Annualised Loss Expectancy (ALE)** is:
- A. $800
- B. $8,000
- C. $80,000
- D. $800,000

**Answer: B.** **ALE = SLE × ARO = 80,000 × 0.1 = $8,000/year.** A control costing less than that and reducing the ALE is cost-justified. See [Domain 5](../domains/05-security-program-management-oversight.md).

**Q36.** Buying cyber-insurance to cover potential breach losses is which risk strategy?
- A. Avoid
- B. Mitigate
- C. Transfer
- D. Accept

**Answer: C.** Shifting financial risk to a third party (insurer) is **risk transfer**. Mitigation adds controls; avoidance stops the activity. See [Domain 5](../domains/05-security-program-management-oversight.md).

**Q37.** The **Recovery Point Objective (RPO)** primarily drives:
- A. How fast a service must be restored
- B. How much data loss (in time) is acceptable, and thus backup frequency
- C. The mean time between failures
- D. The cost of a penetration test

**Answer: B.** **RPO** is the maximum tolerable **data loss** measured in time, which dictates how often you back up. **RTO** is the restore-time target. See [Domain 5](../domains/05-security-program-management-oversight.md).

**Q38.** In privacy law, the party that **determines the purposes and means** of processing personal data is the:
- A. Data processor
- B. Data controller
- C. Data custodian
- D. Data subject

**Answer: B.** The **controller** decides *why and how* data is processed; the **processor** acts on the controller's instructions; the **subject** is the individual the data is about. See [Domain 5](../domains/05-security-program-management-oversight.md).

**Q39.** Which agreement is the **umbrella contract** of general terms under which specific future work is ordered?
- A. Service Level Agreement (SLA)
- B. Memorandum of Understanding (MOU)
- C. Master Service Agreement (MSA)
- D. Non-Disclosure Agreement (NDA)

**Answer: C.** An **MSA** sets overarching terms; specific deliverables are then ordered via a **Statement of Work (SOW)**. An SLA defines service levels; an MOU is a soft statement of intent. See [Domain 5](../domains/05-security-program-management-oversight.md).

**Q40.** A document that defines measurable service levels (such as 99.9% uptime) and penalties for missing them is a(n):
- A. NDA
- B. SLA
- C. BPA
- D. MOU

**Answer: B.** A **Service Level Agreement (SLA)** specifies measurable performance commitments and remedies. See [Domain 5](../domains/05-security-program-management-oversight.md).

**Q41.** Which governance document is **recommended but optional** rather than mandatory?
- A. Policy
- B. Standard
- C. Procedure
- D. Guideline

**Answer: D.** **Guidelines** offer optional best-practice advice. Policies, standards, and procedures are mandatory. See [Domain 5](../domains/05-security-program-management-oversight.md).

**Q42.** The central log that records each identified risk with its likelihood, impact, owner, and treatment is the:
- A. Risk register
- B. Audit committee charter
- C. Business impact analysis
- D. Acceptable use policy

**Answer: A.** The **risk register** is the single source of truth for tracking risks and their status. See [Domain 5](../domains/05-security-program-management-oversight.md).

**Q43.** "How much risk an organisation is willing to take to meet its objectives" defines its:
- A. Risk tolerance
- B. Risk appetite
- C. Risk threshold
- D. Residual risk

**Answer: B.** **Risk appetite** is the amount of risk an organisation is willing to accept; **tolerance** is the acceptable variation around it; the **threshold** is the trigger line. See [Domain 5](../domains/05-security-program-management-oversight.md).

**Q44.** Investigating a vendor's financial stability and security posture **before** signing is best described as:
- A. Due care
- B. Due diligence
- C. Attestation
- D. Right to audit

**Answer: B.** **Due diligence** is the investigation done *before* acting; **due care** is the reasonable, ongoing effort afterwards. See [Domain 5](../domains/05-security-program-management-oversight.md).

**Q45.** A penetration test in which the tester is given **no prior information** about the target environment is:
- A. Known-environment (white-box)
- B. Partially known (grey-box)
- C. Unknown-environment (black-box)
- D. A compliance audit

**Answer: C.** An **unknown-environment (black-box)** test mimics an external attacker with no inside knowledge. See [Domain 5](../domains/05-security-program-management-oversight.md) and [../../ceh/00-overview/legal-and-ethics.md](../../ceh/00-overview/legal-and-ethics.md).

**Q46.** A data subject's right to have their personal data erased on request is the:
- A. Right to be forgotten
- B. Right of access
- C. Right to portability
- D. Right to rectification

**Answer: A.** The **right to be forgotten** (right to erasure) lets individuals request deletion of their personal data. See [Domain 5](../domains/05-security-program-management-oversight.md).

**Q47.** Which is a likely **consequence of non-compliance** with a regulation?
- A. Improved reputation
- B. Regulatory fines and possible loss of license
- C. Automatic certification
- D. Reduced audit scope

**Answer: B.** Non-compliance can bring **fines, sanctions, reputational damage, contractual penalties, and loss of license**. See [Domain 5](../domains/05-security-program-management-oversight.md).

**Q48.** An audit performed by an **independent outside firm** for objective, formal assurance is a(n):
- A. Self-assessment
- B. Internal audit
- C. External (independent third-party) audit
- D. Risk register review

**Answer: C.** An **independent third-party** external audit gives the most objective assurance and is used for formal certification. See [Domain 5](../domains/05-security-program-management-oversight.md).

**Q49.** Running simulated phishing emails against staff and tracking who clicks is part of:
- A. Penetration testing of firewalls
- B. A security awareness program
- C. Disaster recovery
- D. Change management

**Answer: B.** Phishing **campaigns**, recognition, and reporting are core to **security awareness**, which develops and executes user training. See [Domain 5](../domains/05-security-program-management-oversight.md).

**Q50.** Reconnaissance during a penetration test that gathers only **public** information without touching the target is:
- A. Active reconnaissance
- B. Passive reconnaissance
- C. Privilege escalation
- D. Lateral movement

**Answer: B.** **Passive recon** uses open sources (WHOIS, public records) without interacting with the target; **active recon** sends packets to it. See [Domain 5](../domains/05-security-program-management-oversight.md).

**Q51.** A formal, signed statement that an organisation accepts a specific risk despite policy is best called:
- A. Risk transfer
- B. Risk acceptance with an exemption/exception
- C. Risk avoidance
- D. Risk mitigation

**Answer: B.** **Acceptance with an exemption/exception** documents and signs off the decision to tolerate a residual risk — not silent inaction. See [Domain 5](../domains/05-security-program-management-oversight.md).

**Q52.** Which metric expresses the average time it takes to **repair and restore** a failed component?
- A. RTO
- B. RPO
- C. MTTR
- D. MTBF

**Answer: C.** **Mean Time To Repair/Recover (MTTR)** is the average repair time; **MTBF** is the average time *between* failures (reliability). See [Domain 5](../domains/05-security-program-management-oversight.md).

---

## Where to go next

- [study-plan.md](./study-plan.md) — the weight-prioritised schedule these questions support.
- [cheat-sheet.md](./cheat-sheet.md) — ports, control types, crypto facts, and the risk formulas these lean on.
- [../domains/README.md](../domains/README.md) — the five domain pages written to the objectives.
- [../00-overview/exam-and-objectives.md](../00-overview/exam-and-objectives.md) — exam format and the objectives PDF.
- [../reference/acronyms.md](../reference/acronyms.md) — full acronym expansions.

## Sources

- CompTIA — Security+ (SY0-701) exam objectives, the five domains and concepts: https://www.comptia.org/en-us/certifications/security/
- NIST — SP 800-61 Computer Security Incident Handling Guide (incident-response lifecycle) and SP 800-30 (risk assessment, SLE/ALE/ARO): https://csrc.nist.gov/
- Sibling hub pages: [../domains/README.md](../domains/README.md) · [../../foundations/core-concepts-least-privilege-jit-zero-trust.md](../../foundations/core-concepts-least-privilege-jit-zero-trust.md) · [../../ceh/00-overview/legal-and-ethics.md](../../ceh/00-overview/legal-and-ethics.md)
- Verified ground truth for this hub: SY0-701; max 90 questions (MCQ + PBQ); 90 minutes; passing 750 on a 100–900 scale; domain weights 12 / 22 / 18 / 28 / 20 percent.
- These practice questions are original study aids for this hub and are **not** CompTIA exam items.
