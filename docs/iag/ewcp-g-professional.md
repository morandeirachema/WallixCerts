# eWCP-G / WCP-G — WALLIX Certified Professional – IAG

Online certification for **WALLIX IAG** (Identity & Access Governance). Covers a standard
IAG project lifecycle from scoping through go-live and recertification campaigns.

| | |
|---|---|
| **Code** | `eWCP-G` (catalog) · `WCP-G` (website) |
| **Level** | Professional |
| **Product** | WALLIX IAG (ex-Kleverware) |
| **Duration** | ~21 hours (online, estimated) |
| **Format** | Online e-learning |
| **Prerequisite** | **No PAM prerequisite.** Windows Server basics recommended |
| **Exam** | Final MCQ, **70% to pass** |
| **Status** | ✅ Available |

## Target audience

Engineers / IT staff deploying WALLIX IAG. (No separate audience line is stated in
sources.)

## Prerequisites

- Technical knowledge of **Windows Server basics**; system/network/infrastructure
  fundamentals recommended.
- Training materials in technical English; **administrator rights** on the laptop required.
- *Unlike the IDaaS/OT tracks, **no PAM/WCP-P prerequisite is listed**.*

## Objective

Introduce, install, and guide through the WALLIX IAG solution — key concepts and
functionalities for a **standard deployment**.

## Curriculum / modules

| # | Module | Topics & labs |
|---|--------|---------------|
| 1 | **Scoping** | How to kick off an IAG project |
| 2 | **Iteration 00 (intro)** | Install client components; files transformation; create data model; set up portal V0; customer workshop · *Labs 2.1–2.4* |
| 3 | **Iteration 01** | Additional portal work: apply filters; integrate application data; workshop; IAG schedule · *Labs 3.1–3.3* |
| 4 | **Qualification & go-live** | Production configuration users; support go-live; operational acceptance testing · *Lab 4.1: server management and migration* |
| 5 | **Product launch** | Administer the portal; runtime management / data analysis; certify campaign (recertification); certify movements · *Labs 5.1–5.3* |
| 6 | **Customer support** | — |

## Lab environment

Labs via **OVA**. Minimum **16 GB RAM, i5, 50 GB free**; reserve ≥ 2 cores and 4 GB RAM
in VirtualBox. **1 preconfigured VM** (Windows Server 2012).

## Scope, exam focus & study tips

> *Study guidance **derived** from the published curriculum and product documentation —
> not official WALLIX exam content; question count and weighting are not published.*

**Scope — what eWCP-G validates:** that you can run a **standard WALLIX IAG project
lifecycle** — scope it, install the client components, transform source files into a data
model, stand up the portal, integrate application data, go live, and operate
**recertification (certify campaign / certify movements)** campaigns.

**Likely focus areas (mapped from the modules):**
- **Scoping** an IAG project and the **iteration-based** delivery method (Modules 1–3).
- **Installing client components**, **files transformation**, and **creating the data
  model** — the **ETL** consolidation step (Module 2 / Iteration 00).
- Building and refining the **portal**: apply **filters** and **integrate application
  data** (Iteration 01).
- **Qualification & go-live**: production user configuration, support, operational
  acceptance testing, **server management and migration** (Module 4).
- **Product launch**: administer the portal, runtime management / **data analysis**, and —
  the headline topic — **certify campaign (recertification)** and **certify movements**
  (Module 5).

**Study tips:**
- Read the technical companion first: the
  [WALLIX IAG — Identity & Access Governance deep dive](../../deep-dives/iag-identity-governance.md) —
  it expands the concepts behind the project lifecycle (the four pillars, ETL, data model,
  JML, campaigns, remediation, PAG) with Mermaid diagrams.
- Be able to state **IAG (governance) vs IAM (management)** in one sentence, and that IAG
  **does not enforce in real time** — remediation is routed to **PAM / ITSM / IAM**.
- Know the **four pillars**: identification/modelization, **Joiner-Mover-Leaver**
  lifecycle, risk control (**SoD / toxic combinations**, orphan & over-entitled accounts),
  and audit & recertification.
- Be able to **walk a recertification campaign** (scope → review items → certify/revoke →
  remediation → compliance report) and a **JML** flow (recertify at **mover**, zero orphan
  accounts at **leaver**).
- Understand why the **ETL** ingests a **read-only consolidated copy** of entitlements, and
  what **PAG (IGA + PAM)** means for governing privileged accounts.

## Assessment

Pre-test; MCQs and hands-on labs throughout; **final MCQ exam, 70% to pass** → WALLIX
Certified Professional – IAG (`eWCP-G`).

> **Not specified in any WALLIX source:** the **number of exam questions**, the **exam
> time limit**, the **certification validity/renewal** period, and the **price**. Confirm
> with WALLIX Academy (`academy@wallix.com`).

## Sources

- WALLIX Academy: https://www.wallix.com/support-services/wallix-academy/
- Training catalog 2025–2026 (EN): https://www.wallix.com/wp-content/uploads/2024/04/WALLIX_TRAINING_2025-2026_ENG.pdf
- WALLIX IAG product page: https://www.wallix.com/products/identity-and-access-governance/
