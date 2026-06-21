# CEH Glossary

> 🔁 This is the **CEH / offensive** glossary. For PAM, identity & WALLIX terms, see the
> [WALLIX glossary](../../../reference/glossary.md) — the two are complementary, not duplicated.

An alphabetical glossary of ethical-hacking and Certified Ethical Hacker (CEH) terms, each defined concisely **in CEH context**. Offensive techniques are defined neutrally with a defensive framing — you learn them to detect and stop them. For acronym expansions, see the [acronyms reference](acronyms.md).

Cross-links point to the relevant CEH v13 module under [../domains/](../domains/) and to the overview docs under [../00-overview/](../00-overview/). Module filenames follow the official 20-module structure; if a target page does not yet exist, the link records where the topic belongs.

> Note for a sysadmin: many terms below (services, hashes, directories, sessions) are everyday administration concepts seen from the attacker's side. Read the definition, then ask "how would I detect or prevent this on a box I run?"

## A

- **Access control** — Mechanisms (authentication + authorisation) that decide who may do what. Broken access control is a top web risk; see [Hacking Web Applications](../domains/14-hacking-web-applications.md).
- **Active reconnaissance** — Information gathering that directly interacts with the target (e.g., scanning, banner grabbing), which can be logged or detected. Contrast *passive reconnaissance*. See [Scanning Networks](../domains/03-scanning-networks.md).
- **Adversary** — Any individual or group attempting to compromise a system; modelled in CEH so defenders can anticipate behaviour. See *threat actor*.
- **Advanced Persistent Threat (APT)** — A skilled, well-resourced adversary that establishes and maintains stealthy long-term access, the model behind much offensive methodology.
- **Attack surface** — The total set of points where an attacker could try to enter or extract data (open ports, services, inputs, users). Reducing it is a core defensive goal; mapped during [Footprinting and Reconnaissance](../domains/02-footprinting-and-reconnaissance.md).
- **Attack vector** — The specific path or method used to reach a target (e.g., phishing email, exposed RDP, vulnerable web form).
- **Authentication** — Proving identity (something you know/have/are). Strengthened by multi-factor authentication (MFA).
- **Authorisation** — Deciding what an authenticated identity is allowed to do. (Distinct from authentication.)
- **Authorisation (legal)** — The explicit written permission that makes hacking *ethical*; without it, the same actions are crimes. See [legal-and-ethics.md](../00-overview/legal-and-ethics.md).

## B

- **Backdoor** — A hidden method of bypassing normal authentication to regain access to a system. Attackers plant them to maintain access; defenders hunt for them. See [System Hacking](../domains/06-system-hacking.md).
- **Banner grabbing** — Reading the identifying text a service returns (version, software) to fingerprint it during scanning/enumeration. See [Enumeration](../domains/04-enumeration.md).
- **Black-box testing** — A test where the tester has no prior internal knowledge of the target, simulating an outside attacker.
- **Black-hat hacker** — An attacker who acts maliciously and without authorisation (contrast *white-hat*, *grey-hat*).
- **Botnet** — A network of compromised hosts ("bots") controlled by an attacker, often used for distributed denial-of-service (DDoS) or spam. See [Denial-of-Service](../domains/10-denial-of-service.md).
- **Brute force** — Trying many candidate values (passwords, keys, tokens) until one works. Countered by lockouts, rate-limiting, and strong secrets. See [System Hacking](../domains/06-system-hacking.md).
- **Buffer overflow** — Writing more data than a buffer holds, corrupting memory and potentially allowing code execution. A classic exploitation primitive.

## C

- **Command and Control (C2)** — The channel/infrastructure an attacker uses to direct compromised hosts. Detecting C2 traffic is a key blue-team task.
- **Confidentiality, Integrity, Availability (CIA triad)** — The three core security goals every control ultimately serves.
- **Covering tracks** — The fifth phase of hacking: removing logs and artifacts to avoid detection. Tamper-evident logging defends against it. See [five-phases-of-hacking.md](../00-overview/five-phases-of-hacking.md).
- **Credential** — A secret (password, hash, key, token) used to authenticate; a primary target of attackers.
- **Cross-Site Request Forgery (CSRF)** — Forcing a logged-in user's browser to send unwanted authenticated requests. See [Hacking Web Applications](../domains/14-hacking-web-applications.md).
- **Cross-Site Scripting (XSS)** — Injecting attacker-controlled script that runs in other users' browsers. See [Hacking Web Applications](../domains/14-hacking-web-applications.md).
- **Cryptography** — The science of protecting data via encryption, hashing, and signatures. Its own module: [Cryptography](../domains/20-cryptography.md).

## D

- **Defence in depth** — Layering multiple, independent controls so no single failure is catastrophic.
- **Denial of Service (DoS)** — Making a service unavailable by exhausting its resources; distributed form is DDoS. See [Denial-of-Service](../domains/10-denial-of-service.md).
- **Dictionary attack** — A password attack using a curated wordlist of likely candidates (faster than full brute force).
- **DNS enumeration** — Querying the Domain Name System to discover hosts, records, and infrastructure during recon.
- **Dumpster diving** — Recovering useful information from discarded materials; a low-tech reconnaissance technique.

## E

- **Encryption** — Transforming data so only holders of a key can read it; the basis of confidentiality.
- **Enumeration** — Actively extracting detailed information (users, shares, services, versions) from a target after scanning. See [Enumeration](../domains/04-enumeration.md).
- **Ethical hacker** — A professional who tests systems with authorisation, in scope, to improve security. See [what-is-ceh.md](../00-overview/what-is-ceh.md).
- **Evasion** — Techniques to avoid detection by IDS/IPS, firewalls, antivirus, or honeypots. See [Evading IDS, Firewalls, and Honeypots](../domains/12-evading-ids-firewalls-honeypots.md).
- **Exploit** — Code or a technique that takes advantage of a vulnerability to produce an unintended effect (e.g., code execution).

## F

- **False positive / false negative** — A false positive is a benign event flagged as malicious; a false negative is a real threat missed. Tuning detection means balancing the two.
- **Firewall** — A control that permits/denies traffic by rules; evading and testing firewalls is a CEH topic. See [Evading IDS, Firewalls, and Honeypots](../domains/12-evading-ids-firewalls-honeypots.md).
- **Footprinting** — The first, largely passive phase of gathering information about a target's people, technology, and exposure. See [Footprinting and Reconnaissance](../domains/02-footprinting-and-reconnaissance.md).
- **Fuzzing** — Sending malformed or random input to find crashes and vulnerabilities in software.

## G

- **Gaining access** — The third phase of hacking: exploiting a weakness to obtain a foothold. See [five-phases-of-hacking.md](../00-overview/five-phases-of-hacking.md).
- **Grey-box testing** — A test with partial internal knowledge (e.g., a standard user account), between black-box and white-box.
- **Grey-hat hacker** — Someone who operates between ethical and malicious — often acting without authorisation but without malicious intent.

## H

- **Hash** — A fixed-length fingerprint of data produced by a one-way function; used for integrity checks and password storage. See [Cryptography](../domains/20-cryptography.md).
- **Honeypot** — A decoy system designed to attract and study attackers and to alert defenders. See [Evading IDS, Firewalls, and Honeypots](../domains/12-evading-ids-firewalls-honeypots.md).

## I

- **Indicator of Compromise (IOC)** — Forensic evidence (hashes, IPs, domains, artifacts) suggesting a breach; the currency of detection and threat intelligence.
- **Injection** — Inserting attacker-controlled data that an interpreter executes as code/commands (e.g., SQL injection, command injection).
- **Intrusion Detection System (IDS)** — Monitors and alerts on suspicious activity (an IPS can also block it).

## K

- **Keylogger** — Software/hardware that records keystrokes to steal credentials and data; a malware/maintaining-access technique. See [Malware Threats](../domains/07-malware-threats.md).
- **Kill chain** — A model of the ordered stages of an attack (e.g., Lockheed Martin's Cyber Kill Chain); useful for disrupting attacks early.

## L

- **Lateral movement** — Moving from one compromised host to others inside a network to expand access. Detect via anomalous internal authentication. See *pivoting*.
- **Living off the land** — Abusing legitimate, already-present tools (e.g., built-in OS utilities) to avoid dropping detectable malware.

## M

- **Maintaining access** — The fourth phase of hacking: keeping a foothold (e.g., via backdoors, persistence). See [five-phases-of-hacking.md](../00-overview/five-phases-of-hacking.md).
- **Malware** — Malicious software (viruses, worms, trojans, ransomware, RATs). Its own module: [Malware Threats](../domains/07-malware-threats.md).
- **Man-in-the-Middle (MITM)** — Secretly relaying or altering traffic between two parties. See [Sniffing](../domains/08-sniffing.md).

## N

- **Non-repudiation** — Assurance that an action cannot later be denied, typically via logging and digital signatures.
- **Null session** — An unauthenticated connection (historically to Windows SMB) that could leak information; a classic enumeration weakness. See [Enumeration](../domains/04-enumeration.md).

## O

- **Open-Source Intelligence (OSINT)** — Intelligence gathered from publicly available sources during footprinting. See [Footprinting and Reconnaissance](../domains/02-footprinting-and-reconnaissance.md).
- **OWASP Top 10** — The Open Worldwide Application Security Project's list of the most critical web-application risks; a reference for the web modules.

## P

- **Passive reconnaissance** — Information gathering with no direct interaction with the target (e.g., public records, search engines), so it is hard to detect.
- **Patch management** — Keeping software updated to remove known vulnerabilities; a foundational defence a sysadmin already practises.
- **Payload** — The part of an exploit or malware that performs the intended action (e.g., a reverse shell). See [System Hacking](../domains/06-system-hacking.md).
- **Penetration test** — An authorised, scoped simulated attack to find and demonstrate exploitable weaknesses, with a report and remediation advice.
- **Persistence** — Mechanisms that let an attacker survive reboots and re-establish access (part of maintaining access).
- **Phishing** — A social-engineering attack using deceptive messages to steal credentials or deliver malware. See [Social Engineering](../domains/09-social-engineering.md).
- **Pivoting** — Using a compromised host as a relay to reach networks not directly accessible to the attacker. Closely related to *lateral movement*.
- **Privilege escalation** — Gaining higher rights than initially granted — *vertical* (e.g., user → admin) or *horizontal* (another user's access). See [System Hacking](../domains/06-system-hacking.md).
- **Proof of Concept (PoC)** — A minimal demonstration that a vulnerability is exploitable, short of full weaponisation.

## R

- **Ransomware** — Malware that encrypts data and demands payment for recovery. See [Malware Threats](../domains/07-malware-threats.md).
- **Reconnaissance** — The first phase of hacking: gathering information about the target. Includes footprinting (active and passive). See [Footprinting and Reconnaissance](../domains/02-footprinting-and-reconnaissance.md).
- **Remote Code Execution (RCE)** — Running arbitrary code on a remote system — among the most severe vulnerability outcomes.
- **Reverse shell** — A connection initiated *from* the victim back to the attacker, often to bypass inbound firewall rules. A common payload type.
- **Risk** — The combination of a threat exploiting a vulnerability and the resulting impact; security work prioritises by risk.
- **Rootkit** — Malware that hides its presence (and an attacker's) deep in a system, often at kernel level, to maintain stealthy access. See [Malware Threats](../domains/07-malware-threats.md).
- **Rules of Engagement (RoE)** — The agreed scope, limits, timing, and authorisation for an engagement. See [legal-and-ethics.md](../00-overview/legal-and-ethics.md).

## S

- **Sandbox** — An isolated environment for safely executing/analysing untrusted code or malware without risking the host.
- **Scanning** — Probing a target to discover live hosts, open ports, and services; the second phase of hacking. See [Scanning Networks](../domains/03-scanning-networks.md).
- **Scope** — The explicit boundary of what may be tested in an engagement; acting outside scope is unauthorised.
- **Session hijacking** — Taking over a valid user session, often by stealing or predicting a session token. See [Session Hijacking](../domains/11-session-hijacking.md).
- **Sniffing** — Capturing and inspecting network traffic; passive (read-only) or active (e.g., with ARP spoofing). See [Sniffing](../domains/08-sniffing.md).
- **Social engineering** — Manipulating people into divulging information or taking unsafe actions. Its own module: [Social Engineering](../domains/09-social-engineering.md).
- **Spoofing** — Falsifying an identifier (IP, MAC, email sender, caller ID) to impersonate a trusted source.
- **SQL Injection (SQLi)** — Injecting attacker-controlled SQL into a database query. Its own module: [SQL Injection](../domains/15-sql-injection.md).
- **Steganography** — Hiding data within other data (e.g., a file inside an image) to conceal its existence.

## T

- **Threat** — A potential cause of an unwanted incident (e.g., malware, an insider, a natural event).
- **Threat actor** — The entity behind a threat — from script kiddies to organised crime to nation-states. See *adversary*.
- **Threat intelligence** — Curated information about adversaries, their TTPs, and IOCs, used to anticipate and detect attacks.
- **Trojan** — Malware disguised as legitimate software to trick a user into running it. See [Malware Threats](../domains/07-malware-threats.md).
- **TTP (Tactics, Techniques, and Procedures)** — The behavioural pattern of an adversary; mapped in frameworks like MITRE ATT&CK.

## V

- **Virus** — Malware that attaches to files/programs and spreads when they run. Contrast a *worm*.
- **Vulnerability** — A weakness that could be exploited to compromise security; identified and rated in [Vulnerability Analysis](../domains/05-vulnerability-analysis.md).
- **Vulnerability assessment** — A systematic review to identify and prioritise vulnerabilities (broader and less intrusive than a penetration test).

## W

- **White-box testing** — A test where the tester has full internal knowledge (source, architecture, credentials), maximising coverage.
- **White-hat hacker** — An authorised, ethical security professional (the role CEH trains for). Contrast *black-hat*, *grey-hat*.
- **Worm** — Self-propagating malware that spreads across networks without needing a host file or user action. See [Malware Threats](../domains/07-malware-threats.md).

## Z

- **Zero-day** — A vulnerability unknown to the vendor (and so unpatched) at the time it is exploited; an exploit for it is a "zero-day exploit."
- **Zombie** — A compromised host enrolled in a botnet and remotely controlled by an attacker.

## Where to go next

- [acronyms.md](acronyms.md) — categorised acronym expansions.
- [what-is-ceh.md](../00-overview/what-is-ceh.md) and [five-phases-of-hacking.md](../00-overview/five-phases-of-hacking.md) — the methodology these terms support.
- [../career/ceh-career-and-adjacent-certs.md](../career/ceh-career-and-adjacent-certs.md) — roles and adjacent certifications.

## Sources

- EC-Council, CEH v13 program and 20-module curriculum — https://www.eccouncil.org/train-certify/certified-ethical-hacker-ceh/
- OWASP (Open Worldwide Application Security Project), OWASP Top 10 — https://owasp.org/Top10/
- MITRE ATT&CK (TTPs) — https://attack.mitre.org/
- NIST glossary of information-security terms (general definitions cross-checked) — https://csrc.nist.gov/glossary
- Lockheed Martin Cyber Kill Chain — https://www.lockheedmartin.com/en-us/capabilities/cyber/cyber-kill-chain.html
