<div align="center">

# 🔐 WallixCerts

### A source-grounded study hub for **Privileged Access Management** & the **WALLIX certifications**

*From “what is PAM?” to certified* — concepts, real diagrams, labs, exam prep, and a
career roadmap for a **systems administrator moving into cybersecurity**.

**A multi-certification study collection** — WALLIX / PAM (primary) · [CEH v13](ceh/README.md)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Docs](https://img.shields.io/badge/docs-40%2B%20pages-blue)
![Diagrams](https://img.shields.io/badge/diagrams-Mermaid-ff3670)
![Focus](https://img.shields.io/badge/focus-Privileged%20Access%20Management-1f6feb)
![Vendor](https://img.shields.io/badge/vendor-WALLIX-orange)
![Facts](https://img.shields.io/badge/facts-source--grounded-success)

</div>

---

> [!NOTE]
> **Unofficial & no fabrication.** A community study compilation, not a WALLIX
> publication. Every factual claim is tied to an official WALLIX document or a reputable
> source (cited per page); unknowns are marked *“not specified in sources.”* Confirm
> current details with WALLIX Academy (`academy@wallix.com`). Compiled **2026-06-17**.

## 🗺️ The learning path

```mermaid
flowchart LR
    F["1 · Foundations<br/>PAM concepts"] --> P["2 · Prerequisites<br/>Linux · AD · net · crypto"]
    P --> D["3 · Products & Certs<br/>the WALLIX suite + tracks"]
    D --> DD["4 · Deep Dives<br/>Bastion internals"]
    DD --> L["5 · Labs<br/>hands-on practice"]
    L --> E["6 · Exam Prep<br/>plan · questions · cheat sheet"]
    E --> C["7 · Career<br/>sysadmin → PAM specialist"]
    R["📚 Reference<br/>glossary · acronyms · compliance"] -.-> F
    R -.-> DD
    R -.-> E
```

## 📦 What's inside

| # | Section | Start here |
|---|---------|-----------|
| 1 | **Foundations** — what PAM is, threats, core principles, market | [foundations/](foundations/README.md) |
| 2 | **Prerequisites** — Linux · Windows/AD · networking · crypto/PKI | [prerequisites/](prerequisites/README.md) |
| 3 | **Products & Certifications** — the WALLIX suite & cert tracks | [product portfolio](docs/00-overview/product-portfolio.md) · [framework](docs/00-overview/certification-framework.md) |
| 4 | **Deep dives** — WALLIX Bastion internals (8 docs) | [deep-dives/](deep-dives/README.md) |
| 5 | **Labs** — build a lab & guided exercises | [labs/](labs/README.md) |
| 6 | **Exam prep** — study plan, 54 practice Qs, cheat sheet | [exam-prep/](exam-prep/README.md) |
| 7 | **Career** — roadmap & adjacent certifications | [career/](career/README.md) |
| 📚 | **Reference** — glossary, acronyms, compliance, sources | [reference/](reference/README.md) |
| 🔌 | **Protocols** — how Kerberos, RADIUS, AD, LDAP & TLS actually work (mechanisms, encryption, diagrams) | [protocols/](protocols/README.md) |

## 🧭 Other certification content in this repo

Beyond WALLIX / PAM, this repo hosts a second full self-study hub plus concise orientation
pages — all built to the same standards (Mermaid diagrams, source-grounded, no fabrication):

- 🎯 **[Certified Ethical Hacker (CEH)](ceh/README.md)** — a **defense-oriented** EC-Council
  **CEH v13** hub: the 20 modules, the 5 phases, tools, safe-lab guidance, exam prep, and a
  glossary/acronyms. Educational & authorized-use only.
- 🧩 **[Adjacent certifications](adjacent-certs/README.md)** — concise overviews of CompTIA
  Security+, OSCP / PNPT, CISSP, and cloud security (Azure AZ-500 / AWS).
- 🗺️ **[Learning roadmap](learning-roadmap.md)** — how foundations, WALLIX/PAM, CEH, and the
  adjacent certs fit into one cyber-career path.
- ⚔️ **[Attack → Defense matrix](attack-to-defense-matrix.md)** — maps common attack
  techniques (from CEH, with MITRE ATT&CK IDs) to the PAM/WALLIX controls that stop them.
  The concrete bridge between the offensive and defensive hubs.

## 🎓 The WALLIX certification framework

Three progressive levels across product tracks. Code format `WC{level}-{track}`;
an `e` prefix means e-learning. Exam model: a final **MCQ requiring 70% to pass**.

```mermaid
flowchart LR
    WCA["WCA — Administrator<br/>understand & operate"] --> WCP["WCP — Professional<br/>deploy & administer"] --> WCE["WCE — Expert<br/>advanced & complex"]
```

| Track | Product | Administrator | Professional | Expert |
|-------|---------|---------------|--------------|--------|
| **PAM / Bastion** | WALLIX Bastion | [WCA-P](docs/pam-bastion/wca-p-administrator.md) | [WCP-P](docs/pam-bastion/wcp-p-professional.md) | [WCE-P](docs/pam-bastion/wce-p-expert.md) |
| **IAG** | WALLIX IAG | [WCA-G](docs/iag/wca-g-administrator.md) *(soon)* | [WCP-G](docs/iag/ewcp-g-professional.md) | — |
| **IDaaS** | WALLIX One IDaaS (Trustelem) | — | [WCP-I](docs/idaas/ewcp-i-professional.md) | — |
| **OT** | WALLIX PAM4OT | — | [eWCP-P-OT](docs/ot-pam4ot/ewcp-p-ot-professional.md) | — |

<details>
<summary>📂 <b>Full repository layout</b></summary>

```mermaid
flowchart LR
    Root["📦 WallixCerts/"]
    Root --> F["foundations/<br/>concepts · threats · principles · market"]
    Root --> Pre["prerequisites/<br/>Linux · Windows/AD · networking · crypto"]
    Root --> Docs["docs/<br/>certifications & product portfolio"]
    Root --> DD["deep-dives/<br/>Bastion internals (8 docs)"]
    Root --> Labs["labs/<br/>setup · exercises"]
    Root --> Exam["exam-prep/<br/>plan · questions · cheat sheet"]
    Root --> Career["career/<br/>roadmap · adjacent certs"]
    Root --> Ref["reference/<br/>glossary · acronyms · compliance · sources"]
    Docs --> Ov["00-overview/"]
    Docs --> PB["pam-bastion/<br/>WCA-P · WCP-P · WCE-P"]
    Docs --> OT["ot-pam4ot/<br/>eWCP-P-OT"]
    Docs --> ID["idaas/<br/>eWCP-I / WCP-I"]
    Docs --> IAG["iag/<br/>eWCP-G / WCP-G · WCA-G"]
```
</details>

## 🔗 Quick links

- 🎓 [WALLIX Academy](https://www.wallix.com/support-services/wallix-academy/)
- 📘 [Official training catalog 2025–2026 (PDF)](https://www.wallix.com/wp-content/uploads/2024/04/WALLIX_TRAINING_2025-2026_ENG.pdf)
- 🧱 [Product portfolio technical overview](docs/00-overview/product-portfolio.md)
- 🧠 [Glossary](reference/glossary.md) · [Acronyms](reference/acronyms.md)
- 📚 [Full source list](reference/sources.md)

## 🤝 Contributing & license

Contributions welcome — see **[CONTRIBUTING.md](CONTRIBUTING.md)** (the no-fabrication
rule, page conventions, and a periodic verification checklist). Licensed under
**[MIT](LICENSE)**.

> Not affiliated with or endorsed by WALLIX. “WALLIX”, “Bastion”, “Trustelem”, “BestSafe”
> and related names are trademarks of their respective owners, used here for
> identification and educational purposes only.
