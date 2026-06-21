# CySA+ (CS0-003) Practice Questions (Unofficial)

A bank of **45+ multiple-choice practice questions** grouped by the four CompTIA Cybersecurity Analyst (CySA+) CS0-003 domains, each with the correct answer and a short explanation that links to the relevant page in this hub. They include **CVSS-reasoning** and **log-analysis** style items to mirror the analysis-heavy nature of the real exam.

> **Unofficial practice questions — NOT real CompTIA exam questions.** These are pedagogical study aids written for this hub to rehearse documented CySA+ concepts (SOC analysis, Common Vulnerability Scoring System (CVSS), NIST incident response, MITRE ATT&CK, SIEM/EDR). They are **not** drawn from, affiliated with, or endorsed by CompTIA, and they do **not** reproduce any actual exam item. The real exam is **a maximum of 85 questions (multiple-choice + performance-based) in 165 minutes**; passing is **750 on a 100–900 scaled score** — *verify on CompTIA*.

## How to use these

1. **Cover the answers.** Read the question, commit to an option, *then* reveal the answer line.
2. **Read the explanation even when you are right** — on CySA+ the *reasoning* (why this log line, why this CVSS metric) is the point, not the letter.
3. **Track misses by domain.** If you miss two or more in a domain, re-read that [domain page](../domains/README.md) before moving on.
4. **Practise the analysis, not just recall.** For the CVSS and log items, work the data by hand before checking — that *is* the PBQ skill.
5. **Simulate pressure.** In your final week, answer in timed blocks (the real exam averages ~1.9 minutes per item).
6. **Pair with the** [study-plan.md](./study-plan.md) **schedule and the** [../reference/glossary.md](../reference/glossary.md) **for the terms these lean on.**

> **Acronyms** are expanded on first use. A consolidated SOC/blue-team list lives in [../reference/glossary.md](../reference/glossary.md); for general security acronyms see the [Security+ acronyms](../../security-plus/reference/acronyms.md).

---

## Domain 1 — Security Operations (33%)

**Q1.** A platform that aggregates, correlates, and alerts on log and event data from many sources is a:
- A. Data Loss Prevention (DLP) system
- B. Web Application Firewall (WAF)
- C. Security Information and Event Management (SIEM) system
- D. Cloud Access Security Broker (CASB)

**Answer: C.** A **SIEM** centralises log collection, correlation, and alerting and is the analyst's primary console. See [Domain 1](../domains/01-security-operations.md).

**Q2.** Which framework breaks an intrusion into four linked features — **adversary, capability, infrastructure, and victim**?
- A. Cyber Kill Chain
- B. MITRE ATT&CK
- C. Diamond Model of Intrusion Analysis
- D. OWASP Top 10

**Answer: C.** The **Diamond Model** links adversary, capability, infrastructure, and victim for each event. The Kill Chain is phase-based; ATT&CK is a technique matrix. See [Domain 1](../domains/01-security-operations.md).

**Q3.** A globally accessible knowledge base of adversary **tactics and techniques** organised by attack phase, widely used to map observed behaviour, is:
- A. CVSS
- B. MITRE ATT&CK
- C. STIX/TAXII
- D. The CISA KEV catalog

**Answer: B.** **MITRE ATT&CK** catalogs real-world tactics, techniques, and procedures (TTPs) so analysts can map behaviour to a known technique ID. See [Domain 1](../domains/01-security-operations.md).

**Q4.** An **Indicator of Compromise (IoC)** differs from an **Indicator of Attack (IoA)** in that an IoC primarily describes:
- A. The attacker's intent in real time
- B. Forensic artefacts showing a breach has already occurred
- C. A predicted future exploit probability
- D. A business risk appetite

**Answer: B.** An **IoC** is evidence of a compromise that **happened** (a malicious hash, IP, or domain); an **IoA** focuses on **behaviour in progress** revealing intent. See [Domain 1](../domains/01-security-operations.md).

**Q5.** A host on the internal network sends a small, regular outbound HTTPS request to the same external IP every 60 seconds, around the clock. This pattern most likely indicates:
- A. Normal software-update checks
- B. A volumetric Distributed Denial of Service (DDoS)
- C. A port scan of the host
- D. Command-and-control (C2) beaconing

**Answer: D.** Regular, fixed-interval outbound connections to one destination are classic **C2 beaconing**. The regularity and small size are the tell. See [Domain 1](../domains/01-security-operations.md).

**Q6.** A proactive search through systems and data for threats that have **evaded existing detections**, often starting from a hypothesis, is called:
- A. Vulnerability scanning
- B. Penetration testing
- C. Patch management
- D. Threat hunting

**Answer: D.** **Threat hunting** is hypothesis-driven and proactive, assuming a breach may already exist rather than waiting for an alert. See [Domain 1](../domains/01-security-operations.md).

**Q7.** Curated information about adversaries, their TTPs, and IoCs — gathered to inform defence — is called:
- A. A risk register
- B. A configuration baseline
- C. Cyber Threat Intelligence (CTI)
- D. A service-level agreement

**Answer: C.** **CTI** is processed, contextual knowledge about threats that drives detection and prioritisation. See [Domain 1](../domains/01-security-operations.md).

**Q8.** Examine this authentication log excerpt for one account:
```
10:00:01 LOGIN FAIL user=jdoe src=203.0.113.9
10:00:02 LOGIN FAIL user=jdoe src=203.0.113.9
10:00:03 LOGIN FAIL user=jdoe src=203.0.113.9
...   (250 failures in 90 seconds) ...
10:01:31 LOGIN SUCCESS user=jdoe src=203.0.113.9
```
The pattern most strongly suggests:
- A. A successful password-spraying campaign against many users
- B. A brute-force attack that ultimately succeeded
- C. Normal user behaviour after a forgotten password
- D. A Distributed Denial of Service against the login service

**Answer: B.** Hundreds of rapid failures for **one** account from **one** source, ending in success, is a **brute-force** that worked. Password spraying targets **many** accounts with few attempts each. See [Domain 1](../domains/01-security-operations.md).

**Q9.** A tool that monitors endpoints, records process and file activity, and can isolate a host or roll back changes during an incident is:
- A. A SIEM
- B. A firewall
- C. A vulnerability scanner
- D. Endpoint Detection and Response (EDR)

**Answer: D.** **EDR** provides deep endpoint telemetry plus response actions such as host isolation. **XDR** extends this across network, cloud, and identity. See [Domain 1](../domains/01-security-operations.md).

**Q10.** A SOC wants to reduce manual triage by automating enrichment and response steps through codified workflows. The right tool category is:
- A. SOAR (Security Orchestration, Automation, and Response)
- B. DLP
- C. PKI (Public Key Infrastructure)
- D. IPS

**Answer: A.** **SOAR** executes playbooks that automate repetitive analyst tasks (enrichment, ticketing, containment). See [Domain 1](../domains/01-security-operations.md).

**Q11.** A web-server access log shows:
```
GET /products?id=1' OR '1'='1 HTTP/1.1  200
```
This request is an attempt at:
- A. Cross-site scripting (XSS)
- B. SQL injection (SQLi)
- C. Directory traversal
- D. Server-Side Request Forgery (SSRF)

**Answer: B.** The `' OR '1'='1` payload in a query parameter is a textbook **SQL injection** probe. The `200` response warrants investigation of whether it succeeded. See [Domain 1](../domains/01-security-operations.md).

**Q12.** An alert fires on benign activity that was **not** actually malicious. This is a:
- A. True positive
- B. False positive
- C. False negative
- D. True negative

**Answer: B.** A **false positive** flags benign activity as malicious; tuning detections reduces it. A **false negative** is a real threat that was **missed** — the more dangerous error. See [Domain 1](../domains/01-security-operations.md).

**Q13.** A DNS log shows thousands of queries to long, random-looking subdomains of one domain (e.g. `a8f3k2.example.com`, `z9q1m7.example.com`). This is a likely sign of:
- A. A legitimate Content Delivery Network (CDN)
- B. A reverse DNS lookup sweep
- C. DNS tunnelling / exfiltration
- D. DNSSEC validation

**Answer: C.** High volumes of random subdomains to a single domain are characteristic of **DNS tunnelling**, often used for covert C2 or **data exfiltration**. See [Domain 1](../domains/01-security-operations.md).

**Q14.** When mapping an intrusion to the **Cyber Kill Chain**, an attacker emailing a weaponised document to a target sits in which phase?
- A. Reconnaissance
- B. Weaponization
- C. Delivery
- D. Actions on Objectives

**Answer: C.** Transmitting the weaponised payload to the victim is the **Delivery** phase. Building the payload is **Weaponization**; the final goal is **Actions on Objectives**. See [Domain 1](../domains/01-security-operations.md).

**Q15.** Two SIEM rules each fire on the same benign scheduled job every night, drowning real alerts. The best first response is to:
- A. Disable the SIEM
- B. Ignore all alerts from that host
- C. Re-image the host
- D. Tune the rules to suppress or whitelist the known-benign job

**Answer: D.** **Tuning** to suppress the known-good activity reduces false positives and **alert fatigue** without blinding the SOC. See [Domain 1](../domains/01-security-operations.md).

**Q16.** An analyst captures suspicious traffic and inspects individual packets to confirm a payload. The most appropriate tool type is:
- A. A password cracker
- B. A protocol/packet analyser (e.g. a network sniffer)
- C. A vulnerability scanner
- D. A SOAR playbook

**Answer: B.** **Packet/protocol analysis** lets the analyst inspect raw traffic to confirm what a connection actually carried. See [Domain 1](../domains/01-security-operations.md).

---

## Domain 2 — Vulnerability Management (30%)

**Q17.** In the **CVSS v3.1** vector `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`, the `AV:N` component means the vulnerability is:
- A. Exploitable only with local access
- B. Exploitable over the network (remotely)
- C. Of network-administrative severity
- D. Already patched by the vendor

**Answer: B.** **AV:N** = Attack Vector: Network, meaning remote exploitation. Combined with low complexity, no privileges, and no user interaction, this vector trends toward **critical**. See [Domain 2](../domains/02-vulnerability-management.md).

**Q18.** Two vulnerabilities both have a CVSS **base score of 9.8**. Vulnerability A appears in the **CISA Known Exploited Vulnerabilities (KEV)** catalog; B does not. The analyst should generally:
- A. Treat them identically because the base scores match
- B. Prioritise B, because unknown risks are worse
- C. Prioritise A, because it is being actively exploited in the wild
- D. Ignore both until the next quarterly cycle

**Answer: C.** A matching base score measures **severity**, not **exploitation**. Presence in the **KEV catalog** is evidence of active exploitation, raising real-world priority. See [Domain 2](../domains/02-vulnerability-management.md).

**Q19.** The **Exploit Prediction Scoring System (EPSS)** adds which dimension that the CVSS base score alone does not capture?
- A. The asset's monetary value
- B. The probability that a vulnerability will be exploited in the near term
- C. The legal liability of a breach
- D. The patch's file size

**Answer: B.** **EPSS** estimates the **likelihood of exploitation** in the wild, complementing CVSS severity for better prioritisation. See [Domain 2](../domains/02-vulnerability-management.md).

**Q20.** Which CVSS metric group lets an organisation adjust a score for its **own** context, such as the importance of the affected asset?
- A. Base
- B. Temporal
- C. Environmental
- D. Exploitability

**Answer: C.** The **Environmental** metric group tailors the score to the organisation's deployment (e.g. modified impact, security requirements). **Base** is intrinsic; **Temporal** reflects exploit maturity over time. See [Domain 2](../domains/02-vulnerability-management.md).

**Q21.** A vulnerability scan that uses valid login credentials to inspect a system from the inside is a:
- A. Non-credentialed scan
- B. Passive scan
- C. Compliance attestation
- D. Credentialed scan

**Answer: D.** A **credentialed scan** authenticates to the target, yielding far more accurate, lower-false-positive results than a **non-credentialed** external view. See [Domain 2](../domains/02-vulnerability-management.md).

**Q22.** A scanner reports a critical vulnerability, but manual verification shows the affected service is not even installed. This finding is a:
- A. True positive
- B. False positive
- C. False negative
- D. Zero-day

**Answer: B.** A reported issue that does not actually exist is a **false positive**. Validating findings before remediation is core to vulnerability analysis. See [Domain 2](../domains/02-vulnerability-management.md).

**Q23.** Which scan type observes traffic without sending probes to targets, avoiding any impact on fragile systems?
- A. Active scan
- B. Credentialed scan
- C. Authenticated scan
- D. Passive scan

**Answer: D.** A **passive scan** analyses existing traffic and never injects probes, making it safe for sensitive or **Operational Technology (OT)** environments. See [Domain 2](../domains/02-vulnerability-management.md).

**Q24.** Place the vulnerability-management lifecycle stages in order:
- A. Remediate → Identify → Report → Prioritise
- B. Report → Remediate → Identify → Analyse
- C. Identify → Analyse/Prioritise → Remediate → Validate/Report
- D. Prioritise → Validate → Identify → Remediate

**Answer: C.** The cycle runs **identify (scan) → analyse and prioritise (e.g. CVSS/EPSS/KEV) → remediate or mitigate → validate and report**, then repeats. See [Domain 2](../domains/02-vulnerability-management.md).

**Q25.** A critical vulnerability cannot be patched immediately because the vendor fix breaks a business application. The best interim response is to:
- A. Accept the risk silently and move on
- B. Apply a compensating control (e.g. network segmentation or a virtual patch) and document it
- C. Take the entire network offline
- D. Delete the scan finding

**Answer: B.** When patching is not yet feasible, a documented **compensating control** reduces exposure until remediation. See [Domain 2](../domains/02-vulnerability-management.md).

**Q26.** A standardised identifier such as **CVE-2024-12345** refers to:
- A. A scoring formula for severity
- B. A class of software weakness
- C. An exploit toolkit
- D. A single, publicly catalogued vulnerability

**Answer: D.** A **CVE (Common Vulnerabilities and Exposures)** ID names one specific, publicly disclosed vulnerability. A **CWE** names the broader weakness **class**; **CVSS** scores severity. See [Domain 2](../domains/02-vulnerability-management.md).

**Q27.** In the CVSS vector, a change from `UI:N` to `UI:R` will generally make the base score:
- A. Higher, because user interaction adds risk
- B. Lower, because requiring user interaction makes exploitation harder
- C. Unchanged, because UI is not scored
- D. Critical regardless of other metrics

**Answer: B.** **UI:R** (User Interaction: Required) means the victim must do something for the exploit to work, which **lowers** exploitability and the score versus **UI:N** (None). See [Domain 2](../domains/02-vulnerability-management.md).

**Q28.** An analyst must reduce false positives and gain visibility into installed software versions on each host. The most effective scanning approach is:
- A. An unauthenticated external scan
- B. An agent-based or credentialed scan
- C. A passive traffic capture only
- D. A single ping sweep

**Answer: B.** **Agent-based** or **credentialed** scanning inspects hosts from the inside, giving accurate software inventory and fewer false positives. See [Domain 2](../domains/02-vulnerability-management.md).

**Q29.** Which factor would most appropriately **raise** an organisation's remediation priority for a vulnerability beyond its raw CVSS base score?
- A. The vulnerable host is an isolated, decommissioned test box
- B. The CVE was published several years ago
- C. The vulnerability is on an internet-facing server **and** listed in the CISA KEV catalog
- D. The scanner used was non-credentialed

**Answer: C.** **Internet exposure plus confirmed active exploitation (KEV)** sharply increases real-world risk, justifying faster remediation. See [Domain 2](../domains/02-vulnerability-management.md).

**Q30.** A scanner misses a real vulnerability that later causes a breach. With respect to detection, this is a:
- A. False positive
- B. False negative
- C. True positive
- D. True negative

**Answer: B.** A real weakness the scanner **failed to detect** is a **false negative** — the costliest blind spot in vulnerability management. See [Domain 2](../domains/02-vulnerability-management.md).

**Q31.** The practice of comparing a system's configuration against a documented secure standard to find drift is best described as:
- A. Penetration testing
- B. A configuration / compliance scan against a baseline
- C. Threat hunting
- D. Tokenisation

**Answer: B.** A **configuration (compliance) scan** measures a host against a secure **baseline** (e.g. a CIS Benchmark) to surface drift and missing hardening. See [Domain 2](../domains/02-vulnerability-management.md).

---

## Domain 3 — Incident Response and Management (20%)

**Q32.** Which order matches the standard NIST-aligned incident-response lifecycle?
- A. Detection → Preparation → Containment → Eradication → Recovery → Post-Incident
- B. Preparation → Detection & Analysis → Containment, Eradication & Recovery → Post-Incident Activity
- C. Containment → Detection → Preparation → Recovery → Eradication → Lessons Learned
- D. Preparation → Recovery → Detection → Containment → Eradication

**Answer: B.** NIST SP 800-61 defines **Preparation → Detection & Analysis → Containment, Eradication & Recovery → Post-Incident Activity**. See [Domain 3](../domains/03-incident-response-and-management.md).

**Q33.** During an active ransomware outbreak, the **first** priority among these is to:
- A. Write the lessons-learned report
- B. Calculate the annualised loss expectancy
- C. Contain the spread (e.g. isolate affected hosts/segments)
- D. Notify the press

**Answer: C.** **Containment** stops the incident from spreading before eradication and recovery. Reporting and lessons learned come later. See [Domain 3](../domains/03-incident-response-and-management.md).

**Q34.** A documented, step-by-step set of procedures for responding to a specific incident type (e.g. phishing) is best called a:
- A. Risk register
- B. Service-level agreement
- C. Configuration baseline
- D. Playbook / runbook

**Answer: D.** A **playbook (runbook)** codifies the response steps for a scenario so analysts act consistently and quickly. See [Domain 3](../domains/03-incident-response-and-management.md).

**Q35.** When collecting digital evidence, the principle of **order of volatility** says you should capture:
- A. Disk images before anything else
- B. Backups before live memory
- C. The most volatile data (e.g. RAM, running processes) first
- D. Logs only after rebooting

**Answer: C.** Capture the **most volatile data first** (CPU/registers, RAM, network state) because it disappears soonest; disks and backups persist longer. See [Domain 3](../domains/03-incident-response-and-management.md).

**Q36.** The documented, unbroken record of who handled evidence, when, and why — preserving its admissibility — is the:
- A. Chain of custody
- B. Risk appetite
- C. Service catalogue
- D. Attack surface

**Answer: A.** **Chain of custody** maintains evidence integrity and accountability so it holds up in legal or HR proceedings. See [Domain 3](../domains/03-incident-response-and-management.md).

**Q37.** After an incident is resolved, identifying the underlying cause (not just the symptom) so it does not recur is:
- A. Containment
- B. Root-cause analysis
- C. Eradication
- D. Reconnaissance

**Answer: B.** **Root-cause analysis** during post-incident activity finds the true cause and feeds lessons learned. See [Domain 3](../domains/03-incident-response-and-management.md).

**Q38.** The time an attacker remains undetected inside an environment, from initial compromise to detection, is called:
- A. Dwell time
- B. Recovery Time Objective
- C. Mean Time Between Failures
- D. Exposure factor

**Answer: A.** **Dwell time** measures how long a threat went undetected; reducing it is a core SOC goal. See [Domain 3](../domains/03-incident-response-and-management.md) and the [glossary](../reference/glossary.md).

**Q39.** During eradication of a malware incident, simply deleting the malicious file is often insufficient because the attacker may have established:
- A. A valid software licence
- B. A service-level agreement
- C. A compliance baseline
- D. Persistence mechanisms (e.g. scheduled tasks, new accounts, registry run keys)

**Answer: D.** Effective **eradication** must remove **persistence** so the attacker cannot regain a foothold after the obvious artefact is deleted. See [Domain 3](../domains/03-incident-response-and-management.md).

**Q40.** Which containment approach lets analysts observe an attacker's behaviour while limiting harm, at the cost of some ongoing risk?
- A. Immediate full disconnection of all systems
- B. Isolation into a monitored/segmented environment (e.g. a sandbox or honeynet)
- C. Deleting all logs
- D. Ignoring the incident

**Answer: B.** **Isolation into a monitored segment** (sandboxing/honeynet) preserves visibility into TTPs while constraining impact. See [Domain 3](../domains/03-incident-response-and-management.md).

---

## Domain 4 — Reporting and Communication (17%)

**Q41.** A metric expressing the **average time from the start of an incident to its detection** is:
- A. Mean Time To Detect (MTTD)
- B. Mean Time To Respond (MTTR)
- C. Recovery Point Objective (RPO)
- D. Annualised Rate of Occurrence (ARO)

**Answer: A.** **MTTD** measures detection speed; **MTTR** measures how quickly the team responds/remediates after detection. Both are key SOC performance metrics. See [Domain 4](../domains/04-reporting-and-communication.md).

**Q42.** When briefing **executive leadership** on a security incident, the report should emphasise:
- A. Raw packet captures and full log dumps
- B. CVSS vector strings for every finding
- C. The exact registry keys modified
- D. Business impact, risk, and recommended decisions in clear, non-technical language

**Answer: D.** Executives need **business impact and decisions**, not deep technical artefacts; tailoring the message to the audience is a Domain 4 skill. See [Domain 4](../domains/04-reporting-and-communication.md).

**Q43.** A vulnerability-management report intended to demonstrate adherence to a regulation or framework is a:
- A. Compliance report
- B. Packet capture
- C. Threat-intelligence feed
- D. Penetration-test scope document

**Answer: A.** A **compliance report** shows the organisation meets a required standard (e.g. PCI DSS, HIPAA) and is a standard reporting output. See [Domain 4](../domains/04-reporting-and-communication.md).

**Q44.** Defining **who** must be informed, and at what severity threshold, during an incident is the purpose of an:
- A. Escalation path / communication plan
- B. Exposure factor
- C. Configuration baseline
- D. Air gap

**Answer: A.** An **escalation path** (in the communication plan) defines stakeholders and triggers so the right people are notified at the right time. See [Domain 4](../domains/04-reporting-and-communication.md).

**Q45.** Sharing observed **Indicators of Compromise (IoCs)** with partners and Information Sharing and Analysis Centers (ISACs) in a structured format most often uses:
- A. STIX/TAXII
- B. CVSS
- C. RADIUS
- D. SAML

**Answer: A.** **STIX** (the data format) over **TAXII** (the transport) is the standard for machine-readable threat-intelligence and IoC sharing. See [Domain 4](../domains/04-reporting-and-communication.md).

**Q46.** A remediation report's **action plan** primarily communicates:
- A. The attacker's full identity
- B. What fixes are required, who owns them, and by when
- C. The marketing strategy
- D. The CEO's salary

**Answer: B.** An **action plan** assigns concrete remediation tasks, owners, and timelines so findings translate into fixes. See [Domain 4](../domains/04-reporting-and-communication.md).

**Q47.** Producing **metrics and Key Performance Indicators (KPIs)** such as time-to-remediate and percentage of critical vulnerabilities closed serves mainly to:
- A. Replace the incident-response plan
- B. Encrypt data at rest
- C. Demonstrate program effectiveness and drive continuous improvement
- D. Conduct reconnaissance

**Answer: C.** Reporting **metrics/KPIs** shows whether the security program is improving and informs leadership decisions and resourcing. See [Domain 4](../domains/04-reporting-and-communication.md).

**Q48.** After an incident closes, the document that captures what happened, what worked, and what to improve is the:
- A. Lessons-learned / after-action report
- B. Acceptable use policy
- C. Vector string
- D. Risk appetite statement

**Answer: A.** The **lessons-learned (after-action) report** feeds back into preparation, closing the incident-response loop. See [Domain 4](../domains/04-reporting-and-communication.md) and [Domain 3](../domains/03-incident-response-and-management.md).

---

## Where to go next

- [study-plan.md](./study-plan.md) — the weight-prioritised schedule these questions support.
- [../reference/glossary.md](../reference/glossary.md) — SOC/blue-team terms, CVSS metric groups, and frameworks these lean on.
- [../domains/README.md](../domains/README.md) — the four domain pages written to the objectives.
- [../00-overview/exam-and-objectives.md](../00-overview/exam-and-objectives.md) — exam format and the objectives PDF.
- [../../security-plus/exam-prep/practice-questions.md](../../security-plus/exam-prep/practice-questions.md) — the foundation-level sibling question bank.

## Sources

- CompTIA — Cybersecurity Analyst (CySA+) CS0-003 exam objectives, the four domains and concepts: https://www.comptia.org/en-us/certifications/cybersecurity-analyst/
- NIST — SP 800-61 Computer Security Incident Handling Guide (incident-response lifecycle, order of volatility): https://csrc.nist.gov/pubs/sp/800/61/r2/final
- FIRST — Common Vulnerability Scoring System (CVSS) specification (vector strings, base/temporal/environmental metric groups): https://www.first.org/cvss/
- FIRST — Exploit Prediction Scoring System (EPSS): https://www.first.org/epss/
- CISA — Known Exploited Vulnerabilities (KEV) Catalog: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- MITRE ATT&CK — adversary tactics and techniques knowledge base: https://attack.mitre.org/
- OASIS — STIX/TAXII threat-intelligence sharing standards: https://oasis-open.github.io/cti-documentation/
- Sibling hub pages: [../domains/README.md](../domains/README.md) · [../reference/glossary.md](../reference/glossary.md) · [../../security-plus/exam-prep/practice-questions.md](../../security-plus/exam-prep/practice-questions.md)
- Verified ground truth for this hub: CS0-003; max 85 questions (MCQ + PBQ); 165 minutes; passing 750 on a 100–900 scale; domain weights 33 / 30 / 20 / 17 percent.
- These practice questions are original study aids for this hub and are **not** CompTIA exam items.
