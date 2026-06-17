# WALLIX Academy — Certification Framework

How WALLIX Academy structures its certifications: levels, codes, delivery formats,
and the common exam model. Compiled from the
[2025–2026 training catalog](https://www.wallix.com/wp-content/uploads/2024/04/WALLIX_TRAINING_2025-2026_ENG.pdf)
and the [WALLIX Academy page](https://www.wallix.com/support-services/wallix-academy/).

---

## The three levels

Each certification level is designed to **build upon the previous**, ensuring a
comprehensive understanding from basic administration to advanced deployment.

| Level | Code | Goal | Typical duration (PAM) |
|-------|------|------|------------------------|
| **WALLIX Certified Administrator** | `WCA` | Understand the solution and be able to manage it in day-to-day activities (no install/deploy) | 1 day (7 h) |
| **WALLIX Certified Professional**  | `WCP` | Install, configure, deploy & administer in a standard/classic architecture | 1–3 days |
| **WALLIX Certified Expert**        | `WCE` | Achieve advanced, large-scale & complex deployments | 1–2 days |

## Naming convention

A code reads `W C x - y`, decoded position by position:

| Position | Symbol | Meaning |
|----------|--------|---------|
| 1 | `W` | "WALLIX" |
| 2 | `C` | "Certified" |
| 3 | `x` | **Level:** `A` = Administrator · `P` = Professional · `E` = Expert |
| 4 | `y` | **Track:** `P` = PAM/Bastion · `G` = IAG · `I` = IDaaS · `P-OT` = OT |

- An **`e` prefix** (`eWCA-P`, `eWCP-P`, `eWCE-P`, `eWCP-G`, `eWCP-I`, `eWCP-P-OT`)
  denotes the **self-paced e-learning** variant delivered on the WALLIX Academy platform.
- ⚠️ **Code inconsistency to know:** the **website matrix** uses `WCP-G`, `WCP-I`,
  `eWCP-P OT`; the **catalog datasheets** use `eWCP-G`, `eWCP-I`, `eWCP-P-OT`. These
  refer to the same certifications.

## Tracks (products)

| Track suffix | Product | Levels available |
|--------------|---------|------------------|
| `-P` | WALLIX Bastion (PAM) | WCA-P, WCP-P, WCE-P |
| `-G` | WALLIX IAG (Identity & Access Governance) | WCP-G *(WCA-G coming soon)* |
| `-I` | WALLIX One IDaaS / Trustelem | WCP-I |
| `-P-OT` | WALLIX PAM4OT (Operational Technology) | eWCP-P-OT |

---

## Common exam & assessment model

Applies across all current tracks:

- **Pre-test** at the start of the session.
- **Continuous assessment** throughout: oral questions, MCQs, and hands-on labs.
- **Final exam: a multiple-choice questionnaire (MCQ)** requiring **≥ 70%** to pass and
  earn the certification.
- On success, WALLIX Academy awards a **digital badge and diploma**.

> **Not specified in official sources:** the exact **number of exam questions** and any
> **certification validity / renewal period**. A web snippet suggested "2 years" but this
> could not be confirmed against an authoritative WALLIX document.

## Delivery formats

- **Instructor-led** (codes without `e`): on-site or remote via **Microsoft Teams**.
  - **Inter-company:** participants from multiple companies in one session.
  - **Intra-company:** session reserved for a single company.
- **E-learning / self-paced** (codes with `e` prefix) on the WALLIX Academy platform.
  Requires **administrator rights** on your laptop to install the lab tools.
- ⚠️ **In-person + inter/intra-company delivery is "only available for the PAM trainings."**
  The IAG, IDaaS and OT tracks are delivered as **online e-learning**.

## Prerequisites common themes

- **Technical English** proficiency (course materials are in technical English;
  sessions delivered in EN/FR/DE per the calendar; PAM courses have English subtitles).
- Foundational **system / network / infrastructure** knowledge; for PAM, familiarity
  with **SSH, RDP, proxy concepts, and Linux**.
- **Certification prerequisites between levels/tracks:**
  - **WCE-P** requires a prior **WCP-P** (or eWCP) certification *and* GNU/Linux CLI knowledge.
  - **WCP-I (IDaaS)** and **eWCP-P-OT (OT)** require a prior **WCP-P** (or eWCP) certification.
  - **WCP-G (IAG)** has **no PAM prerequisite** (Windows Server basics recommended).

## Labs

WALLIX provides preconfigured lab environments (Azure-hosted VMs for instructor-led;
downloadable **OVA** images for e-learning). Typical minimum hardware for OVA labs:
**i5 CPU, 32 GB RAM, ~40 GB free disk** (IAG lab: 16 GB RAM / 50 GB free).

---

## Target audience

WALLIX **customers** (end-users) and **reseller partners** — engineers and technicians.
The Expert level (WCE-P) is aimed more specifically at engineers.

## Administrative facts

- **2025 figures:** ~1,062 trainees certified (334 via e-learning), 91% satisfaction,
  1,396 valid certifications.
- WALLIX Academy is a **registered training organization** (FR registration no.
  `11 75 51538 75`). Courses are accessible to people with disabilities.
- **Contact:** `academy@wallix.com`.

## Sources

- WALLIX Academy: https://www.wallix.com/support-services/wallix-academy/
- Training catalog 2025–2026 (EN): https://www.wallix.com/wp-content/uploads/2024/04/WALLIX_TRAINING_2025-2026_ENG.pdf
- Training catalog 2023 PAM4ALL (EN): https://www.wallix.com/wp-content/uploads/2024/02/WALLIX_TRAINING_2023_PAM4ALL_EN.pdf
- WALLIX training landing page: https://www.wallix.com/support/training/
