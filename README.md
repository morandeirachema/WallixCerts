# WallixCerts — WALLIX Academy Certification Documentation

Unofficial study & reference documentation for the certifications offered by
**[WALLIX Academy](https://www.wallix.com/support-services/wallix-academy/)** — the
training and certification arm of [WALLIX](https://www.wallix.com/), the European
(French) cybersecurity vendor specializing in identity and access security.

This repo compiles, from official WALLIX sources, the **technical background**, the
**course curricula**, and the **exam requirements** for each WALLIX certification.

> ⚠️ **Unofficial.** This is a community/study compilation, not a WALLIX publication.
> Always confirm current details with WALLIX Academy (`academy@wallix.com`) and the
> official [training catalog](https://www.wallix.com/wp-content/uploads/2024/04/WALLIX_TRAINING_2025-2026_ENG.pdf).
> Compiled **2026-06-17** from the 2025–2026 catalog and live WALLIX pages.

---

## The certification framework

WALLIX Academy structures its certifications into **three progressive levels**, each
building on the previous, across several **product tracks**. Naming convention:

```
W C x - y
│ │ │   └─ Track:  P = PAM/Bastion · G = IAG · I = IDaaS · P-OT = OT · E = EPM
│ │ └───── Level:  A = Administrator · P = Professional · E = Expert
│ └─────── "Certified"
└───────── "WALLIX"

An "e" prefix (e.g. eWCP-P) denotes the self-paced e-learning variant.
```

| Level | Code | Goal |
|-------|------|------|
| **Administrator** | `WCA` | Understand the solution and manage it in day-to-day activities |
| **Professional**  | `WCP` | Manage deployment & administration in a standard environment |
| **Expert**        | `WCE` | Achieve advanced / large-scale & complex deployments |

**Exam model (all tracks):** a final **multiple-choice (MCQ)** exam requiring a
**70% score** to pass, plus a pre-test and continuous assessment (oral questions,
MCQs, hands-on labs) during the course.

See **[docs/00-overview/certification-framework.md](docs/00-overview/certification-framework.md)** for full details.

---

## Certification matrix

| Track | Product | Administrator | Professional | Expert | Status |
|-------|---------|---------------|--------------|--------|--------|
| **PAM / Bastion** | WALLIX Bastion | [WCA-P](docs/pam-bastion/wca-p-administrator.md) | [WCP-P](docs/pam-bastion/wcp-p-professional.md) | [WCE-P](docs/pam-bastion/wce-p-expert.md) | ✅ Available |
| **IAG** | WALLIX IAG | [WCA-G](docs/iag/wca-g-administrator.md) *(coming soon)* | [WCP-G](docs/iag/ewcp-g-professional.md) | — | 🟡 Partial |
| **IDaaS** | WALLIX One IDaaS (Trustelem) | — | [WCP-I](docs/idaas/ewcp-i-professional.md) | — | ✅ Available |
| **OT** | WALLIX PAM4OT | — | [eWCP-P-OT](docs/ot-pam4ot/ewcp-p-ot-professional.md) | — | ✅ Available |

> The non-PAM tracks (IAG, IDaaS, OT) are delivered as **online e-learning**; only the
> PAM track offers in-person inter-/intra-company classroom delivery. **WCP-I** and
> **eWCP-P-OT** require a prior **WCP-P** certification.

---

## Repository layout

```
WallixCerts/
├── README.md                                  ← you are here
├── docs/
│   ├── 00-overview/
│   │   ├── certification-framework.md          Levels, codes, exam model, formats
│   │   └── product-portfolio.md                Technical overview of all WALLIX products
│   ├── pam-bastion/                            Core PAM track
│   │   ├── README.md
│   │   ├── wca-p-administrator.md
│   │   ├── wcp-p-professional.md
│   │   └── wce-p-expert.md
│   ├── ot-pam4ot/   → eWCP-P-OT
│   ├── idaas/       → eWCP-I (WCP-I)
│   └── iag/         → eWCP-G (WCP-G) + WCA-G
└── reference/
    └── sources.md                              All source URLs, grouped
```

## Quick links

- 🎓 [WALLIX Academy](https://www.wallix.com/support-services/wallix-academy/)
- 📘 [Official training catalog 2025–2026 (PDF)](https://www.wallix.com/wp-content/uploads/2024/04/WALLIX_TRAINING_2025-2026_ENG.pdf)
- 🧱 [Product portfolio technical overview](docs/00-overview/product-portfolio.md)
- 📚 [Full source list](reference/sources.md)
- ✉️ Contact: `academy@wallix.com`
