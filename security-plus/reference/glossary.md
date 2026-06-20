# Security+ Glossary

> 🔁 This is the **CompTIA Security+ (SY0-701)** glossary. For PAM/identity terms see the [WALLIX glossary](../../reference/glossary.md); for offensive / ethical-hacking terms see the [CEH glossary](../../ceh/reference/glossary.md). The three are complementary — where a term is treated in more depth in another hub or a Security+ domain page, the entry cross-links there rather than repeating it.

An alphabetical glossary of CompTIA Security+ terms, each defined **in Security+ exam context** for a sysadmin moving into cybersecurity. The emphasis is on concepts that the exam tests as definitions or scenario distinctions (e.g. due care vs due diligence, RTO vs RPO, fail-open vs fail-closed). For acronym expansions, see [acronyms.md](acronyms.md).

> **No fabrication.** Definitions follow CompTIA's published objectives and the NIST glossary; where a term has a precise NIST/standard meaning it is used. See [Sources](#sources). Numbers in worked examples (e.g. for SLE/ALE) are illustrative, not real figures.

---

## A

**Acceptable Use Policy (AUP)** — A policy defining how employees may use organisational systems and data. A foundational governance document — see [Domain 5](../domains/05-security-program-management-oversight.md).

**Access control models** — The schemes deciding who may do what: **MAC** (system-enforced labels), **DAC** (owner-set permissions), **RBAC** (role-based), **ABAC** (attribute-based), and rule-based. See the [WALLIX glossary RBAC entry](../../reference/glossary.md) for the PAM treatment.

**Air gap** — Physically isolating a system or network from others (no network connection) so it cannot be reached remotely; common in OT/high-security environments.

**Annualized Loss Expectancy (ALE)** — The expected monetary loss from a risk **per year**: `ALE = SLE × ARO`. Drives whether a control's cost is justified. See **Single Loss Expectancy** and [Domain 5](../domains/05-security-program-management-oversight.md).

**Attestation** — A formal, often signed, assertion that something is true — e.g. that controls are in place, that a configuration matches policy, or (in TPM/secure boot) that a platform booted into a known-good state. Used in audits and supply-chain assurance.

**Attack surface** — The total set of points an attacker could target. Hardening, least privilege and segmentation shrink it. See the [WALLIX glossary](../../reference/glossary.md).

**Authentication, Authorization, and Accounting (AAA)** — Proving identity, deciding permitted actions, and recording activity — the backbone of access control. See [acronyms.md](acronyms.md).

## B

**Baseline (configuration baseline)** — A documented, approved standard configuration for a system. Deviations are detected by configuration management and **File Integrity Monitoring**; re-applying it is "baselining."

**Business Continuity Plan (BCP)** — The plan to keep critical **business functions** running during disruption (broader than IT). Contrast **Disaster Recovery Plan**, which restores **IT systems**. See [Domain 4](../domains/04-security-operations.md).

**Business Impact Analysis (BIA)** — The analysis identifying critical functions and the impact of their loss; it produces the **RTO**, **RPO**, MTD and resource needs that drive continuity planning.

**Blast radius** — How much a single compromise can affect. Segmentation and least privilege contain it — see the [WALLIX glossary](../../reference/glossary.md).

## C

**Chain of custody** — The documented, unbroken record of who handled a piece of evidence, when and why, preserving its integrity so it is admissible. Core to **forensics** — see [Domain 4](../domains/04-security-operations.md).

**CIA triad** — **Confidentiality, Integrity, Availability** — the three foundational goals of information security. Many controls map to one or more; **non-repudiation** and authentication are often added.

**Compensating control** — An alternative control used when the primary/required one is not feasible, providing comparable protection (e.g. extra monitoring where MFA cannot be deployed). One of CompTIA's control **types** (preventive, detective, corrective, deterrent, compensating, directive) alongside its **categories** (technical, managerial, operational, physical) — see [Domain 1](../domains/01-general-security-concepts.md).

**Continuity of Operations (COOP)** — A program ensuring an organisation's essential functions continue during a wide-scale disruption.

**Control plane / data plane** — In zero-trust architecture, the **control plane** makes and enforces access decisions (policy engine/administrator) while the **data plane** carries the actual resource traffic. See **Zero Trust**.

## D

**Data at rest / in transit / in use** — The three states data exists in: stored (protect with **FDE**/encryption), moving over a network (protect with **TLS**/IPSec), and being processed in memory (hardest to protect; addressed by enclaves/secure processing).

**Data classification** — Labelling data by sensitivity (e.g. public, internal, confidential, restricted/regulated) so the right controls and handling apply.

**Data controller / data processor** — Under data-protection law (GDPR): the **controller** determines *why and how* personal data is processed and is accountable for it; the **processor** processes data **on the controller's behalf** (e.g. a SaaS vendor). The distinction sets who carries which obligations.

**Data sovereignty** — The principle that data is subject to the **laws of the country where it is physically stored/processed**. Drives where cloud data may reside; related to **data residency** (where data is kept) and **localization** (legal requirement to keep it in-country).

**Defense in depth (layered security)** — Layering multiple independent controls so no single failure is catastrophic. See the [WALLIX glossary](../../reference/glossary.md).

**Disaster Recovery Plan (DRP)** — The plan to restore **IT systems and data** after a disaster; a subset of the broader **BCP**.

**Due care vs due diligence** — **Due care** is taking the reasonable, ongoing actions a prudent organisation would to protect assets (the *doing*). **Due diligence** is the investigation/research that informs those actions and verifies they are working (the *checking* — e.g. vetting a vendor before and during a contract). The exam tests this distinction.

**Defense evasion / fail states** — See **Fail-open / fail-closed**.

## E

**Encryption** — Transforming data so only holders of the key can read it: **symmetric** (one shared key — fast, e.g. AES) and **asymmetric** (public/private key pair — e.g. RSA/ECC). See the [acronyms](acronyms.md#cryptography-pki--hashing) and [Domain 1](../domains/01-general-security-concepts.md).

**Entitlement** — A specific right or permission granted to an identity; governance reviews **right-size** them. See the [WALLIX glossary](../../reference/glossary.md).

**Exposure Factor (EF)** — The percentage of an asset's value lost in a single risk event; multiplied by asset value to get **SLE**.

## F

**Fail-open vs fail-closed (fail-safe vs fail-secure)** — How a control behaves when it fails. **Fail-open** keeps access/traffic flowing (favours **availability** — e.g. a badge reader that unlocks doors in a power cut for safety). **Fail-closed / fail-secure** denies access on failure (favours **security/confidentiality** — e.g. a firewall that blocks all traffic if its ruleset cannot load). The right choice depends on whether safety/availability or security dominates.

**False positive / false negative** — A **false positive** is a benign event flagged as malicious (alert fatigue); a **false negative** is a real threat missed. Detection tuning trades them off; biometrics express this as **FAR/FRR** (see [acronyms](acronyms.md#authentication-identity--access)).

**File Integrity Monitoring (FIM)** — Detecting unauthorised changes to critical files by comparing against a hashed baseline.

**Forensics** — The disciplined collection, preservation and analysis of digital evidence, preserving **chain of custody** and acquisition order (**order of volatility**). See [Domain 4](../domains/04-security-operations.md).

## G

**Gap analysis** — Comparing the current security posture against a desired standard/framework to identify and prioritise what is missing.

**Governance, Risk, and Compliance (GRC)** — Aligning security with business risk and regulatory obligations; the theme of [Domain 5](../domains/05-security-program-management-oversight.md).

## H

**Hardening** — Reducing a system's attack surface by removing unneeded services, closing ports, tightening configuration and applying secure defaults. See the [WALLIX glossary](../../reference/glossary.md).

**Honeypot / honeynet** — A **decoy** system (honeypot) or network (honeynet) deployed to detect, divert and study attackers without exposing real assets. A **honeyfile** and **honeytoken** are decoy data/credentials that should never be touched legitimately, so any access is a high-fidelity alert.

**Hashing** — Producing a fixed-length, one-way digest of data to verify **integrity** (and, with a salt, to store passwords). Unlike encryption it is not reversible. See **Salting** and [acronyms](acronyms.md#cryptography-pki--hashing).

## I

**Incident response lifecycle** — CompTIA's phases: **Preparation → Detection/Analysis → Containment → Eradication → Recovery → Lessons Learned**. See [Domain 4](../domains/04-security-operations.md).

**Indicator of Compromise (IoC)** — Forensic evidence (hashes, IPs, domains, anomalous behaviour) suggesting a breach. Shared via threat-intel feeds.

**Integrity** — Assurance that data has not been altered without authorisation; verified by hashing, digital signatures and FIM. One leg of the **CIA triad**.

## J

**Jump server (jump box / jump host)** — A hardened intermediary host that administrators connect **through** to reach sensitive systems, so they never connect directly. A practical least-privilege/segmentation control — treated in depth in the [WALLIX glossary](../../reference/glossary.md) (where the WALLIX Bastion *is* the jump server/PAM bastion).

**Just-in-Time (JIT) access** — Granting privileged access only at the moment of need, for a limited time, then revoking it. See the [WALLIX glossary](../../reference/glossary.md).

## K

**Key escrow** — Storing a copy of cryptographic keys with a trusted third party so data can be recovered (or lawfully accessed) if the original key is lost. A trade-off between recoverability and exposure risk.

**Key stretching** — Deliberately slowing key/hash derivation (e.g. **PBKDF2**, **bcrypt**, **scrypt**, **Argon2**) to make password cracking expensive. Often paired with **salting**.

## L

**Least privilege (PoLP)** — Granting the minimum rights needed for as short a time as needed. A foundational principle — see the [WALLIX glossary](../../reference/glossary.md) and [Domain 1](../domains/01-general-security-concepts.md).

**Load balancing** — Distributing traffic across multiple servers for **availability** and performance; a resilience control (contrast clustering/failover).

## M

**Mean Time To Repair (MTTR) / Between Failures (MTBF) / To Failure (MTTF)** — Reliability metrics: average time to **repair** a failure, average time **between** failures of a repairable system, and average lifespan of a **non-repairable** item. Inform availability and sparing decisions.

**Multi-factor authentication (MFA)** — Requiring factors from two or more categories: something you **know**, **have**, **are**, plus location/behaviour. See the [WALLIX glossary](../../reference/glossary.md).

## N

**Non-repudiation** — Assurance that a party cannot credibly deny an action, because tamper-resistant, attributable evidence exists (e.g. a **digital signature** or individually-attributed logs). See the [WALLIX glossary](../../reference/glossary.md).

## O

**Order of volatility** — The sequence in which forensic evidence should be collected, **most volatile first** (CPU registers/cache → RAM → network state → disk → backups/archives), because volatile data is lost soonest.

**Obfuscation** — Making data or code harder to interpret without strong cryptographic guarantees. Includes **tokenization**, **data masking**, and **steganography** (hiding data inside other data).

## P

**Patch management** — The controlled process of testing and deploying software updates to remediate vulnerabilities; a core operational control.

**Phishing** — A social-engineering attack using fraudulent messages to steal credentials or deliver malware; variants include spear phishing, whaling, **smishing** (SMS) and **vishing** (voice). See [Domain 2](../domains/02-threats-vulnerabilities-mitigations.md).

**Principle of separation of duties** — See **Separation of duties**.

**Provisioning / deprovisioning** — Creating accounts and access at onboarding/role change, and **removing** them at offboarding (a frequent audit failure when missed). Tied to the **joiner-mover-leaver** lifecycle.

## R

**Recovery Point Objective (RPO)** — The maximum tolerable **data loss**, expressed as time since the last good backup (e.g. "≤ 1 hour" means back up at least hourly). Contrast **RTO**.

**Recovery Time Objective (RTO)** — The maximum tolerable **time to restore** a function after disruption (how long down is acceptable). Set by the **BIA**; together with **RPO** it drives backup and failover design.

**Residual risk** — The risk that **remains after** controls/mitigations are applied. Management formally **accepts** residual risk; it can never reach zero.

**Risk appetite / risk tolerance** — **Appetite** is the broad amount and type of risk an organisation is willing to pursue toward its objectives (often expressed as expansionary, conservative or neutral); **tolerance** is the acceptable variation around that for a specific risk. Both are set by leadership and bound risk decisions. See [Domain 5](../domains/05-security-program-management-oversight.md).

**Risk treatment (response)** — The choice for each risk: **accept**, **avoid**, **transfer** (e.g. insurance/outsourcing), or **mitigate** (reduce). What remains after mitigation is **residual risk**.

**Root Cause Analysis (RCA)** — Post-incident analysis identifying the underlying cause (not just symptoms) so the issue is prevented from recurring.

## S

**Salting** — Adding a unique random value to each password before hashing, so identical passwords hash differently and precomputed (**rainbow table**) attacks fail. Paired with **key stretching**. See [acronyms](acronyms.md#cryptography-pki--hashing).

**Sandboxing** — Running untrusted code/files in an isolated environment to observe behaviour without risking the host; used in malware analysis and email/web filtering.

**Segmentation (network segmentation / microsegmentation)** — Dividing a network into isolated zones (VLANs, subnets, firewalls; microsegmentation goes per-workload) to limit lateral movement and contain breaches. A **defense-in-depth** and **zero-trust** building block.

**Separation of duties (SoD)** — Splitting a sensitive process so no single person controls it end-to-end (e.g. requester ≠ approver), preventing fraud and error. Related to **least privilege** and **dual control** — see the [WALLIX glossary](../../reference/glossary.md).

**Single Loss Expectancy (SLE)** — The expected monetary loss from **one** occurrence of a risk: `SLE = Asset Value × Exposure Factor`. Feeds the annual figure **ALE**. *(Example: a $10,000 asset with a 25% exposure factor gives SLE = $2,500 — illustrative figures.)*

**Service Level Agreement (SLA)** — A contractual commitment to a service level (e.g. 99.9% uptime, response times). One of several agreement types (MOU, MOA, MSA, BPA, NDA, ISA, SOW) tested in [Domain 5](../domains/05-security-program-management-oversight.md).

**Social engineering** — Manipulating people into breaking security (phishing, pretexting, baiting, tailgating, impersonation). The human attack surface — see [Domain 2](../domains/02-threats-vulnerabilities-mitigations.md).

**Steganography** — Concealing data **within** other data (e.g. inside an image) so its very existence is hidden; a form of obfuscation/exfiltration.

## T

**Tabletop exercise** — A discussion-based drill where stakeholders **talk through** their response to a hypothetical incident scenario, validating plans without touching production. Contrast a **simulation** (technical, hands-on) and a **full-scale/failover test**.

**Threat / vulnerability / risk** — A **threat** is a potential cause of harm (actor or event); a **vulnerability** is a weakness it could exploit; **risk** is the likelihood and impact of that happening. Controls reduce risk by addressing vulnerabilities or threats. See [Domain 2](../domains/02-threats-vulnerabilities-mitigations.md).

**Threat intelligence** — Curated information about adversaries, their **TTPs** and **IoCs**, sourced from OSINT, feeds and sharing standards (**STIX/TAXII**) to inform defence.

**Tokenization** — Replacing sensitive data (e.g. a card number) with a non-sensitive **token** that maps back to the original only in a secure vault. Unlike encryption there is no mathematical relationship between token and value, so the token alone is useless to an attacker. Used for **PCI DSS** scope reduction; contrast **masking** (which obscures part of a value for display).

**Trust but verify → never trust, always verify** — The shift in mindset that **Zero Trust** embodies.

## V

**Vulnerability management** — The continuous cycle of **identify (scan) → assess/prioritise (e.g. CVSS) → remediate/mitigate → validate → report** weaknesses. See [Domain 4](../domains/04-security-operations.md).

## W

**Watering hole attack** — Compromising a website a target group is known to visit, so victims infect themselves by browsing it; a targeted, indirect delivery method.

## Z

**Zero-day** — A vulnerability that is exploited **before** a patch or signature exists, so traditional detection misses it; behavioural detection and defense in depth are the mitigations.

**Zero Trust** — A security model assuming **no implicit trust** from network location: *"never trust, always verify."* Every request is authenticated, authorized and continuously evaluated; built from a **policy engine/administrator** (control plane) enforcing access to the **data plane**. See the [WALLIX glossary](../../reference/glossary.md) and NIST SP 800-207.

**Zero Trust Network Access (ZTNA)** — Applying zero trust to connectivity: per-session access to **specific** resources after verification, rather than dropping a user onto the whole network as a VPN does. See the [WALLIX glossary](../../reference/glossary.md).

---

## See also

- [acronyms.md](acronyms.md) — expansions of every abbreviation used above.
- [General Security Concepts (Domain 1)](../domains/01-general-security-concepts.md) · [Threats, Vulnerabilities & Mitigations (Domain 2)](../domains/02-threats-vulnerabilities-mitigations.md) · [Security Architecture (Domain 3)](../domains/03-security-architecture.md) · [Security Operations (Domain 4)](../domains/04-security-operations.md) · [Security Program Management & Oversight (Domain 5)](../domains/05-security-program-management-oversight.md)
- [WALLIX / PAM glossary](../../reference/glossary.md) · [CEH glossary](../../ceh/reference/glossary.md) — the repo's sibling glossaries.
- [Exam format and objectives](../00-overview/exam-and-objectives.md)

## Sources

- CompTIA — Security+ certification page and official **SY0-701 exam objectives** PDF (definitions and term lists): https://www.comptia.org/en-us/certifications/security/ *(download and verify; objectives change per exam version)*
- NIST Computer Security Resource Center — Glossary: https://csrc.nist.gov/glossary
- NIST SP 800-207 — Zero Trust Architecture (control/data plane, policy engine): https://csrc.nist.gov/pubs/sp/800/207/final
- NIST SP 800-61 — Computer Security Incident Handling Guide (IR lifecycle, order of volatility): https://csrc.nist.gov/pubs/sp/800/61/r2/final
- NIST SP 800-34 — Contingency Planning (BIA, RTO/RPO, BCP/DRP): https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final
- NIST SP 800-30 — Guide for Conducting Risk Assessments (risk, SLE/ALE concepts): https://csrc.nist.gov/pubs/sp/800/30/r1/final
- EU General Data Protection Regulation (GDPR) — controller/processor, data protection: https://gdpr-info.eu/
