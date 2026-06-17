# WCA-P — WALLIX Certified Administrator – PAM (Bastion)

**Entry-level** certification for the WALLIX Bastion PAM solution. Covers basic
administration, concepts, and maintenance of WALLIX Bastion and Access Manager —
**excluding installation and deployment** (those start at [WCP-P](wcp-p-professional.md)).

| | |
|---|---|
| **Code** | `WCA-P` (instructor-led) · `eWCA-P` (e-learning) |
| **Level** | Administrator (1 of 3) |
| **Product** | WALLIX Bastion + WALLIX Access Manager |
| **Duration** | 1 day (7 hours) |
| **Formats** | Inter-company, intra-company, online/e-learning |
| **Class size** | 6 trainees max (instructor-led); nominative (e-learning) |
| **Language** | Technical English; PAM courses available with English subtitles |
| **Prerequisite** | None — this is the entry level |
| **Exam** | Final MCQ, **70% to pass** |

## Target audience

Engineers and technicians of WALLIX end-users and reseller partners who want to
understand WALLIX Bastion and be able to **manage it in day-to-day activities**.

## Prerequisites

- Technical knowledge of **SSH, RDP, proxy concepts, and Linux**; proficiency in
  system, network and infrastructure fundamentals. *(Brush up via the repo
  [prerequisites](../../prerequisites/README.md).)*
- **Technical-English** proficiency.
- **Microsoft Teams** (instructor-led). For e-learning, **administrator rights** on
  your laptop to install the lab tools.
- *No prior WALLIX certification required.*

## Objective

Cover basic administration, concepts, and maintenance of the WALLIX Bastion and Access
Manager solution — **excluding installation and deployment**.

## Curriculum / modules

| # | Module | Topics |
|---|--------|--------|
| 0 | **Introduction** | WALLIX presentation |
| 1 | **Installing & Handling** | Introduction, Prerequisites, Connection, Profiles, System, Backup/Restoration, Versioning/Upgrades |
| 2 | **Session Manager** | Introduction, Global concepts, Main configuration, User Access, Applications, Advanced configuration · *Lab 0: Setup DNS; Lab 1: RDP & SSH Connections* |
| 3 | **Password Manager** | Introduction, Global concept, Password visualization, Password Change, Break Glass · *Lab 2: Password checkout* |
| 4 | **Approval** | Introduction, Approval workflow for Session Manager, Approval workflow for Password Manager |
| 5 | **Audit** | Web audit, Session history, Account history, Approval history, Authentication history, Connection statistics, **5.7 Session recording parameters**, **5.8 Management session records** |
| 6 | **Access Manager** | Introduction, Global concepts, **User perspective**, Advanced configuration, Audit from Access Manager |
| 7 | **Customer Support** | Introduction, Before opening a case, Opening a case, After opening a case, Closing a case |

> **Instructor-led vs e-learning:** in the **eWCA-P** (e-learning) variant, the catalog
> lists Module 6 (Access Manager) with **five** sub-modules — it **omits "6.3 User
> perspective"** that the instructor-led WCA-P includes.

## Lab environment

WALLIX provides the labs.
- **Instructor-led:** 4 preconfigured VMs — Domain Controller (Win 2016), Windows
  Server 2016, Linux Server, WALLIX Bastion on Azure. Minimum **8 GB RAM / i5**.
- **E-learning:** labs via **OVA** — minimum **4 CPU / i5, 32 GB RAM, 40 GB free**.

## Study companion — map each module to a deep dive

The deep-dive docs explain the *why* behind the syllabus (all sourced from the official
WALLIX guides):

| Module | Go deeper |
|--------|-----------|
| 1 Installing & Handling | [Bastion architecture](../../deep-dives/bastion-architecture.md) |
| 2 Session Manager | [Session management](../../deep-dives/session-management.md) · [data model](../../deep-dives/bastion-data-model.md) |
| 3 Password Manager | [Secrets & password management](../../deep-dives/secrets-and-password-management.md) |
| 4 Approval | [Session management → approval workflows](../../deep-dives/session-management.md) |
| 5 Audit | [Troubleshooting & logs](../../deep-dives/troubleshooting-and-logs.md) |
| 6 Access Manager | [Authentication & Access Manager](../../deep-dives/authentication-and-access-manager.md) |
| 7 Customer Support | [Troubleshooting & logs → support process](../../deep-dives/troubleshooting-and-logs.md) |

Foundation concepts: [What is PAM?](../../foundations/what-is-pam.md) ·
[core concepts](../../foundations/core-concepts-least-privilege-jit-zero-trust.md).
Self-test: [practice questions](../../exam-prep/practice-questions.md).

## Scope, exam focus & study tips

> *Study guidance **derived** from the published curriculum and the WALLIX product
> documentation — not official WALLIX exam content. The exam's question count and weighting
> are not published.*

**Scope — what WCA-P validates:** that you can **operate an already-deployed** WALLIX
Bastion + Access Manager day to day — connect users to targets over RDP/SSH, manage live
sessions, use the password vault (view / check-out / Break-Glass), set up approval
workflows, read the audit trail and session recordings, use Access Manager, and run the
support process. It deliberately **excludes installation, deployment, and high
availability** (those begin at [WCP-P](wcp-p-professional.md)).

**Likely focus areas (mapped from the modules):**
- Opening RDP and SSH sessions through the Bastion (Module 2).
- Password visualization, check-out, and Break-Glass (Module 3).
- Approval workflows for sessions and passwords (Module 4).
- Navigating audit — session / account / approval / authentication history and recordings (Module 5).
- Access Manager from the user/admin perspective (Module 6).

**Study tips:**
- Actually run the three labs (DNS setup; RDP & SSH; password check-out) — the assessment mirrors hands-on tasks.
- Be crisp on the split between **Session Manager** (brokering connections) and **Password Manager** (the vault).
- Understand what an *authorization* is conceptually (it links *who* to *what*), even though building one is a WCP-P skill.
- Know **Break-Glass** (emergency credential access) and what each audit screen shows.
- Don't over-invest in installation or HA — they're out of scope at this level.

## Assessment

Pre-test at start; **final MCQ exam, 70% to pass** → `WCA-P` / `eWCA-P` certification
(digital badge + diploma). Continuous assessment during the course:
- **Instructor-led (WCA-P):** oral questions, MCQs, and hands-on labs.
- **E-learning (eWCA-P):** MCQs and hands-on labs (no oral questions).

> **Not specified in any WALLIX source:** the exact **number of exam questions**, the
> **exam time limit**, the **certification validity/renewal period**, and the **price**.
> Do not assume these — confirm with WALLIX Academy (`academy@wallix.com`).

## Next step

➡️ [WCP-P — WALLIX Certified Professional](wcp-p-professional.md)

## Sources

- WALLIX Academy: https://www.wallix.com/support-services/wallix-academy/
- Training catalog 2025–2026 (EN) — primary, retrieved full (35 pp.): https://www.wallix.com/wp-content/uploads/2024/04/WALLIX_TRAINING_2025-2026_ENG.pdf
