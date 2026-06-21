# CySA+ Glossary

> 🔁 This is the **CompTIA Cybersecurity Analyst (CySA+) CS0-003** glossary, focused on **Security Operations Center (SOC) / blue-team** terms. For foundational security terms see the [Security+ glossary](../../security-plus/reference/glossary.md) and [Security+ acronyms](../../security-plus/reference/acronyms.md); for Privileged Access Management (PAM) / identity terms see the [WALLIX glossary](../../../reference/glossary.md); for offensive / ethical-hacking terms see the [CEH glossary](../../ceh/reference/glossary.md). The hubs are complementary — where a term is treated more deeply elsewhere, the entry cross-links there rather than repeating it.

An alphabetical glossary of CySA+ terms defined **in CySA+ / SOC analyst context** for a sysadmin moving into a blue-team role. The emphasis is on the analyst's daily vocabulary the exam tests as definitions or scenario distinctions (e.g. IoC vs IoA, false positive vs false negative, CVSS base vs environmental, MTTD vs MTTR). Acronyms are expanded on first use; there is **no full acronym table here** — see the [Security+ acronyms](../../security-plus/reference/acronyms.md) for general expansions and only **CySA+-specific** terms are added below.

> **No fabrication.** Definitions follow CompTIA's published CS0-003 objectives, NIST, FIRST (the Forum of Incident Response and Security Teams), MITRE, and CISA. Where a term has a precise standard meaning it is used. See [Sources](#sources). Any worked figures are illustrative, not real.

---

## A

**Alert fatigue** — The desensitisation that occurs when analysts face too many alerts, especially **false positives**, causing real threats to be missed. Detection **tuning** and **SOAR** automation reduce it. See [Domain 1](../domains/01-security-operations.md).

**Anomaly-based detection** — Detecting threats by flagging deviations from an established **baseline** of normal behaviour, rather than matching known signatures. Catches novel/zero-day activity at the cost of more false positives. Contrast **signature-based detection**. See [Domain 1](../domains/01-security-operations.md).

**Attribution** — The analytical process of identifying the adversary (group, nation-state, or campaign) behind an intrusion, drawing on **TTPs**, infrastructure, and threat intelligence. Often supported by the **Diamond Model**. See [Domain 1](../domains/01-security-operations.md).

## B

**Baseline (behavioural baseline)** — The documented profile of normal activity for a host, user, or network, against which **anomaly-based detection** measures deviation. See the [Security+ glossary](../../security-plus/reference/glossary.md).

**Beaconing** — The regular, often fixed-interval, outbound network traffic a compromised host sends to a **command-and-control (C2)** server. Its periodicity and consistency are key detection signals. See [Domain 1](../domains/01-security-operations.md).

## C

**CISA Known Exploited Vulnerabilities (KEV) catalog** — A list maintained by the U.S. **Cybersecurity and Infrastructure Security Agency (CISA)** of vulnerabilities **confirmed to be actively exploited** in the wild. Presence in the KEV catalog should sharply raise remediation priority regardless of **CVSS** base score. See [Domain 2](../domains/02-vulnerability-management.md).

**Command-and-Control (C2 / C&C)** — The channel an attacker uses to remotely control compromised hosts, issue commands, and exfiltrate data; often revealed by **beaconing**. A late phase of the **Cyber Kill Chain**. See [Domain 1](../domains/01-security-operations.md).

**Common Vulnerabilities and Exposures (CVE)** — A standardised, unique identifier (e.g. `CVE-2024-12345`) for one publicly disclosed vulnerability. Distinct from a **CWE** (the weakness *class*) and **CVSS** (the severity *score*). See [Domain 2](../domains/02-vulnerability-management.md).

**Common Vulnerability Scoring System (CVSS)** — The open standard from **FIRST** for rating vulnerability severity 0.0–10.0 via three metric groups — **base**, **temporal**, and **environmental** (see those entries). A score is expressed as a **vector string** such as `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`. See [Domain 2](../domains/02-vulnerability-management.md).

**CVSS base metrics** — The **intrinsic, unchanging** characteristics of a vulnerability: exploitability (**Attack Vector, Attack Complexity, Privileges Required, User Interaction, Scope**) and impact (**Confidentiality, Integrity, Availability**). They yield the headline base score. See [Domain 2](../domains/02-vulnerability-management.md).

**CVSS temporal metrics** — Metrics that **change over time** — exploit code maturity, remediation level, and report confidence — refining the base score as the threat landscape evolves. See [Domain 2](../domains/02-vulnerability-management.md).

**CVSS environmental metrics** — Metrics that let an organisation **tailor** the score to its own environment (modified impact and security requirements for the affected asset). The same CVE can warrant different priorities in different organisations. See [Domain 2](../domains/02-vulnerability-management.md).

**Credentialed scan** — A vulnerability scan that authenticates to the target with valid credentials, inspecting it from the inside for far more accurate, lower-false-positive results than a **non-credentialed** scan. See [Domain 2](../domains/02-vulnerability-management.md).

**Cyber Kill Chain** — Lockheed Martin's seven-phase model of an intrusion: **Reconnaissance → Weaponization → Delivery → Exploitation → Installation → Command & Control → Actions on Objectives**. Breaking any phase disrupts the attack. See [Domain 1](../domains/01-security-operations.md).

**Cyber Threat Intelligence (CTI)** — Processed, contextual knowledge about adversaries, their **TTPs**, and **IoCs**, sourced from open-source intelligence (OSINT), feeds, and sharing standards (**STIX/TAXII**), used to inform detection and prioritisation. See [Domain 1](../domains/01-security-operations.md).

## D

**Data exfiltration** — The unauthorised transfer of data out of an organisation, often over covert channels such as **DNS tunnelling**, encrypted **C2**, or staged uploads. **Data Loss Prevention (DLP)** and egress monitoring detect it. See [Domain 1](../domains/01-security-operations.md).

**Diamond Model of Intrusion Analysis** — A framework that models each intrusion event as four linked features — **adversary, capability, infrastructure, victim** — to support analysis, correlation, and **attribution**. See [Domain 1](../domains/01-security-operations.md).

**DNS tunnelling** — Encoding data or **C2** traffic inside Domain Name System (DNS) queries/responses to bypass controls; betrayed by high volumes of long, random-looking subdomains. A common **data-exfiltration** technique. See [Domain 1](../domains/01-security-operations.md).

**Dwell time** — The elapsed time from an attacker's initial compromise until detection. Reducing dwell time (and thus **MTTD**) is a primary SOC objective. See [Domain 3](../domains/03-incident-response-and-management.md).

## E

**Endpoint Detection and Response (EDR)** — A tool that continuously records endpoint process, file, and network activity, detects malicious behaviour, and enables response actions such as host isolation and rollback. Extended by **XDR** across more telemetry sources. See [Domain 1](../domains/01-security-operations.md).

**Eradication** — The incident-response phase that removes the threat completely — including **persistence** mechanisms, malware, and attacker accounts — not just the obvious artefact. Follows containment, precedes recovery. See [Domain 3](../domains/03-incident-response-and-management.md).

**Exploit Prediction Scoring System (EPSS)** — A FIRST data-driven model estimating the **probability** that a vulnerability will be exploited in the near term. It complements **CVSS** severity (which measures *impact*, not *likelihood*) for sharper prioritisation. See [Domain 2](../domains/02-vulnerability-management.md).

## F

**False negative** — A real threat or vulnerability that detection **failed to flag**. The most dangerous detection error because it is silent. Contrast **false positive**. See [Domain 1](../domains/01-security-operations.md).

**False positive** — Benign activity incorrectly flagged as malicious, the chief driver of **alert fatigue**. Reduced by **tuning**. Contrast **true positive** (a correctly flagged real threat) and **true negative** (correctly unflagged benign activity). See [Domain 1](../domains/01-security-operations.md).

## H

**Heuristic detection** — Detection that uses rules of thumb and behavioural analysis to identify likely-malicious activity, including previously unseen variants; related to **anomaly-based detection**. See [Domain 1](../domains/01-security-operations.md).

**Honeypot / honeynet** — A decoy system (honeypot) or network (honeynet) deployed to detect and study attackers without exposing real assets; can serve as a monitored **containment** environment. See the [Security+ glossary](../../security-plus/reference/glossary.md).

## I

**Incident response (IR) lifecycle** — The NIST SP 800-61 phases: **Preparation → Detection & Analysis → Containment, Eradication & Recovery → Post-Incident Activity**. The backbone of [Domain 3](../domains/03-incident-response-and-management.md).

**Indicator of Attack (IoA)** — Evidence of an attacker's **intent and behaviour in progress** (e.g. a process spawning a shell then connecting outbound), focusing on *what the adversary is trying to do* rather than static artefacts. Contrast **IoC**. See [Domain 1](../domains/01-security-operations.md).

**Indicator of Compromise (IoC)** — A forensic artefact showing a breach **has occurred** — a malicious file hash, IP, domain, or registry key. Typically shared via **threat intelligence** in **STIX/TAXII** format. Contrast **IoA**. See [Domain 1](../domains/01-security-operations.md).

## K

**Key Performance Indicator (KPI)** — A measurable value showing how effectively the security program meets objectives (e.g. percentage of critical vulnerabilities remediated within the service-level target). Reported to stakeholders in [Domain 4](../domains/04-reporting-and-communication.md).

**Known Exploited Vulnerabilities (KEV)** — See **CISA Known Exploited Vulnerabilities (KEV) catalog**.

## L

**Lateral movement** — An attacker's pivoting from an initial foothold to other systems to reach high-value targets; a key behaviour to detect in **threat hunting** and a MITRE ATT&CK tactic. See [Domain 1](../domains/01-security-operations.md) and the [CEH glossary](../../ceh/reference/glossary.md).

**Lessons-learned (after-action) report** — The post-incident document capturing what happened, what worked, and what to improve, feeding back into **Preparation**. Part of [Domain 3](../domains/03-incident-response-and-management.md) and [Domain 4](../domains/04-reporting-and-communication.md).

**Log analysis** — The core analyst skill of reading and correlating system, network, web, DNS, and authentication logs (often via a **SIEM**) to identify malicious activity. The heart of CySA+ **PBQs**. See [Domain 1](../domains/01-security-operations.md).

## M

**Mean Time To Detect (MTTD)** — The average time from the start of an incident to its detection; a key SOC metric, closely tied to **dwell time**. See [Domain 4](../domains/04-reporting-and-communication.md).

**Mean Time To Respond / Remediate (MTTR)** — The average time from detection to response or remediation. (In reliability contexts MTTR can mean *Mean Time To Repair* — see the [Security+ glossary](../../security-plus/reference/glossary.md).) Reported in [Domain 4](../domains/04-reporting-and-communication.md).

**MITRE ATT&CK** — A globally accessible knowledge base of adversary **tactics and techniques** (e.g. `T1059` Command and Scripting Interpreter) observed in the real world, organised by attack phase. Analysts map observed behaviour to technique IDs for detection, hunting, and reporting. See [Domain 1](../domains/01-security-operations.md).

## N

**Non-credentialed scan** — A vulnerability scan run without login credentials, seeing the target as an outside attacker would. Faster to set up but more prone to **false positives** than a **credentialed scan**. See [Domain 2](../domains/02-vulnerability-management.md).

## O

**Order of volatility** — The sequence for collecting forensic evidence, **most volatile first** (CPU registers/cache → RAM → network state → disk → backups), because volatile data is lost soonest. See [Domain 3](../domains/03-incident-response-and-management.md) and the [Security+ glossary](../../security-plus/reference/glossary.md).

## P

**Packet / protocol analysis** — Inspecting captured network traffic at the packet level (e.g. with a sniffer) to confirm exactly what a connection carried; used to validate alerts and investigate intrusions. See [Domain 1](../domains/01-security-operations.md).

**Passive scan** — A scan that observes existing traffic without sending probes to targets, making it safe for fragile or **Operational Technology (OT)** systems. Contrast **active scan**. See [Domain 2](../domains/02-vulnerability-management.md).

**Persistence** — Mechanisms (scheduled tasks, new accounts, registry run keys, services) an attacker installs to survive reboots and regain access; must be removed during **eradication**. A MITRE ATT&CK tactic. See [Domain 3](../domains/03-incident-response-and-management.md).

**Playbook / runbook** — A documented, step-by-step procedure for responding to a specific scenario (e.g. phishing, ransomware). A **playbook** sets the broader strategy/decision flow; a **runbook** gives the detailed operational steps. Often automated via **SOAR**. See [Domain 3](../domains/03-incident-response-and-management.md).

**Precision vs recall (detection tuning)** — The trade-off behind **false positives** and **false negatives**: tightening a detection cuts false positives (higher precision) but risks missing threats (lower recall), and vice versa. Tuning balances the two. See [Domain 1](../domains/01-security-operations.md).

## R

**Root-cause analysis (RCA)** — Post-incident analysis identifying the **underlying cause** (not just the symptom) so the issue does not recur; feeds the **lessons-learned** report. See [Domain 3](../domains/03-incident-response-and-management.md).

## S

**Sandboxing** — Running an untrusted file or URL in an isolated environment to observe its behaviour safely; used in malware analysis and as a monitored **containment** option. See the [Security+ glossary](../../security-plus/reference/glossary.md).

**Security Information and Event Management (SIEM)** — A platform that **aggregates, correlates, and alerts** on log and event data from across the environment; the analyst's primary console for **log analysis** and detection. See [Domain 1](../domains/01-security-operations.md).

**Security Orchestration, Automation, and Response (SOAR)** — A platform that executes **playbooks** to automate repetitive analyst tasks — enrichment, ticketing, containment — reducing **MTTR** and **alert fatigue**. See [Domain 1](../domains/01-security-operations.md).

**Security Operations Center (SOC)** — The team and facility that monitors, detects, analyses, and responds to security events, typically using **SIEM**, **EDR**, and **SOAR**. The CySA+ analyst's home. See [Domain 1](../domains/01-security-operations.md).

**Signature-based detection** — Detecting known threats by matching against a database of signatures (hashes, patterns, rules). Reliable for known threats but blind to novel ones; complemented by **anomaly-based detection**. See [Domain 1](../domains/01-security-operations.md).

**STIX / TAXII** — **Structured Threat Information eXpression (STIX)** is the standard data format for machine-readable threat intelligence and **IoCs**; **Trusted Automated eXchange of Indicator Information (TAXII)** is the transport that shares it between organisations and **Information Sharing and Analysis Centers (ISACs)**. See [Domain 4](../domains/04-reporting-and-communication.md).

## T

**Tactics, Techniques, and Procedures (TTPs)** — The behavioural fingerprint of an adversary: *tactics* (the goal), *techniques* (how it is achieved), and *procedures* (the specific implementation). Catalogued in **MITRE ATT&CK** and central to **threat hunting** and **attribution**. See [Domain 1](../domains/01-security-operations.md).

**Threat hunting** — The proactive, hypothesis-driven search for threats that have **evaded existing detections**, assuming a breach may already exist rather than waiting for an alert. See [Domain 1](../domains/01-security-operations.md).

**Threat intelligence** — See **Cyber Threat Intelligence (CTI)**.

**True positive / true negative** — A **true positive** is a real threat correctly flagged; a **true negative** is benign activity correctly left unflagged. Together with **false positive/negative** they form the detection-quality matrix. See [Domain 1](../domains/01-security-operations.md).

**Tuning (detection tuning)** — Adjusting detection rules and thresholds to suppress known-benign activity and reduce **false positives** without creating **false negatives**; a continuous SOC activity. See [Domain 1](../domains/01-security-operations.md).

## V

**Vector string (CVSS vector)** — The compact, machine-readable encoding of a **CVSS** score's metric values, e.g. `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`. Reading it is a common CySA+ **PBQ** task. See [Domain 2](../domains/02-vulnerability-management.md).

**Vulnerability management lifecycle** — The continuous cycle of **identify (scan) → analyse and prioritise (CVSS / EPSS / KEV) → remediate or mitigate → validate and report**. The spine of [Domain 2](../domains/02-vulnerability-management.md).

## X

**XDR (Extended Detection and Response)** — An evolution of **EDR** that correlates detection and response across endpoints, network, cloud, identity, and email for unified visibility. See [Domain 1](../domains/01-security-operations.md).

## Z

**Zero-day** — A vulnerability exploited **before** a patch or signature exists, so **signature-based detection** misses it; **anomaly-based detection** and defence in depth are the mitigations. See the [Security+ glossary](../../security-plus/reference/glossary.md).

---

## See also

- [Security Operations (Domain 1)](../domains/01-security-operations.md) · [Vulnerability Management (Domain 2)](../domains/02-vulnerability-management.md) · [Incident Response & Management (Domain 3)](../domains/03-incident-response-and-management.md) · [Reporting & Communication (Domain 4)](../domains/04-reporting-and-communication.md)
- [study-plan.md](../exam-prep/study-plan.md) · [practice-questions.md](../exam-prep/practice-questions.md) — the hub's exam-prep pages.
- [Security+ glossary](../../security-plus/reference/glossary.md) · [Security+ acronyms](../../security-plus/reference/acronyms.md) — foundational terms and full acronym expansions.
- [WALLIX / PAM glossary](../../../reference/glossary.md) · [CEH glossary](../../ceh/reference/glossary.md) — the repo's sibling glossaries.

## Sources

- CompTIA — Cybersecurity Analyst (CySA+) CS0-003 certification page and official exam objectives PDF (definitions and term lists): https://www.comptia.org/en-us/certifications/cybersecurity-analyst/ *(download and verify; objectives change per exam version)*
- NIST — Computer Security Resource Center Glossary: https://csrc.nist.gov/glossary
- NIST — SP 800-61 Computer Security Incident Handling Guide (IR lifecycle, order of volatility): https://csrc.nist.gov/pubs/sp/800/61/r2/final
- FIRST — Common Vulnerability Scoring System (CVSS) specification (base/temporal/environmental metrics, vector strings): https://www.first.org/cvss/
- FIRST — Exploit Prediction Scoring System (EPSS): https://www.first.org/epss/
- CISA — Known Exploited Vulnerabilities (KEV) Catalog: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- MITRE ATT&CK — adversary tactics and techniques knowledge base: https://attack.mitre.org/
- Lockheed Martin — Cyber Kill Chain: https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html
- Caltagirone, Pendergast & Betz — The Diamond Model of Intrusion Analysis: https://www.activeresponse.org/the-diamond-model/
- OASIS — STIX/TAXII threat-intelligence sharing standards: https://oasis-open.github.io/cti-documentation/
