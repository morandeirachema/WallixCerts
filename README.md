# WallixCerts — WALLIX & PAM Certification Study Hub

A complete, **source-grounded** self-study repository for a systems administrator moving
into cybersecurity and specializing in **Privileged Access Management (PAM)** with the
**[WALLIX](https://www.wallix.com/)** suite and its
**[WALLIX Academy](https://www.wallix.com/support-services/wallix-academy/)** certifications.

It takes you from *"what is PAM?"* all the way to certification exam prep and a career
roadmap — concepts, **flow diagrams**, acronyms, deep technical dives, labs, and practice
questions.

> ⚠️ **Unofficial & no fabrication.** This is a community study compilation, not a WALLIX
> publication. Every factual claim is tied to an official WALLIX document or a reputable
> source (cited per page); unknowns are marked *"not specified in sources"* rather than
> guessed. Always confirm current details with WALLIX Academy (`academy@wallix.com`).
> Compiled **2026-06-17**.

---

## How to use this repo — the learning path

```
   ┌──────────────┐   ┌───────────────┐   ┌──────────────────┐   ┌──────────────┐
   │ 1 FOUNDATIONS│──▶│ 2 PREREQUISITES│──▶│ 3 PRODUCTS &     │──▶│ 4 DEEP DIVES │
   │   PAM concepts│   │  sysadmin→cyber│   │   CERTIFICATIONS │   │ Bastion guts │
   └──────────────┘   └───────────────┘   └──────────────────┘   └──────┬───────┘
                                                                         │
        ┌────────────────────────────────────────────────────────────────┘
        ▼
   ┌──────────┐   ┌──────────────┐   ┌──────────┐
   │ 5 LABS   │──▶│ 6 EXAM PREP  │──▶│ 7 CAREER │     (+ REFERENCE throughout)
   │ practice │   │ plan + tests │   │ roadmap  │
   └──────────┘   └──────────────┘   └──────────┘
```

| Step | Section | Start here |
|------|---------|-----------|
| 1 | **Foundations** — what PAM is and why it matters | [foundations/](foundations/README.md) |
| 2 | **Prerequisites** — Linux, AD, networking, crypto | [prerequisites/](prerequisites/README.md) |
| 3 | **Products & Certifications** — the WALLIX suite & cert tracks | [docs/00-overview/](docs/00-overview/product-portfolio.md) · [certification framework](docs/00-overview/certification-framework.md) |
| 4 | **Deep dives** — WALLIX Bastion internals | [deep-dives/](deep-dives/README.md) |
| 5 | **Labs** — build a lab & do exercises | [labs/](labs/README.md) |
| 6 | **Exam prep** — study plan, practice questions, cheat sheet | [exam-prep/](exam-prep/README.md) |
| 7 | **Career** — from sysadmin to PAM specialist | [career/](career/README.md) |
| — | **Reference** — glossary, acronyms, compliance, sources | [reference/](reference/README.md) |

---

## The WALLIX certification framework

Three progressive levels — **Administrator (WCA) → Professional (WCP) → Expert (WCE)** —
across product tracks. Code format `WC{level}-{track}`; `e` prefix = e-learning.
Exam model: a final **MCQ requiring 70% to pass**. Full detail in the
[certification framework](docs/00-overview/certification-framework.md).

| Track | Product | Administrator | Professional | Expert |
|-------|---------|---------------|--------------|--------|
| **PAM / Bastion** | WALLIX Bastion | [WCA-P](docs/pam-bastion/wca-p-administrator.md) | [WCP-P](docs/pam-bastion/wcp-p-professional.md) | [WCE-P](docs/pam-bastion/wce-p-expert.md) |
| **IAG** | WALLIX IAG | [WCA-G](docs/iag/wca-g-administrator.md) *(soon)* | [WCP-G](docs/iag/ewcp-g-professional.md) | — |
| **IDaaS** | WALLIX One IDaaS (Trustelem) | — | [WCP-I](docs/idaas/ewcp-i-professional.md) | — |
| **OT** | WALLIX PAM4OT | — | [eWCP-P-OT](docs/ot-pam4ot/ewcp-p-ot-professional.md) | — |

---

## Repository layout

```
WallixCerts/
├── foundations/      PAM concepts (what/why), threats, core principles, market landscape
├── prerequisites/    Linux · Windows/AD · networking & protocols · crypto & PKI
├── docs/
│   ├── 00-overview/  certification-framework · product-portfolio (technical overview)
│   ├── pam-bastion/  WCA-P · WCP-P · WCE-P
│   ├── ot-pam4ot/    eWCP-P-OT
│   ├── idaas/        eWCP-I / WCP-I
│   └── iag/          eWCP-G / WCP-G (+ WCA-G coming soon)
├── deep-dives/       Bastion architecture, data model, sessions, secrets, auth, HA, API, troubleshooting
├── labs/             home lab setup · hands-on exercises
├── exam-prep/        study plan · practice questions · cheat sheet
├── career/           sysadmin→PAM roadmap · skills & adjacent certs
└── reference/        glossary · acronyms · compliance & standards · sources
```

~40 documents. Each page carries its own **Sources** section.

## Quick links

- 🎓 [WALLIX Academy](https://www.wallix.com/support-services/wallix-academy/)
- 📘 [Official training catalog 2025–2026 (PDF)](https://www.wallix.com/wp-content/uploads/2024/04/WALLIX_TRAINING_2025-2026_ENG.pdf)
- 🧱 [Product portfolio technical overview](docs/00-overview/product-portfolio.md)
- 🧠 [Glossary](reference/glossary.md) · [Acronyms](reference/acronyms.md)
- 📚 [Full source list](reference/sources.md)
- ✉️ Contact: `academy@wallix.com`
