# WCP-P — WALLIX Certified Professional – PAM (Bastion)

The **core deployment-level** certification. Covers **installation, configuration,
deployment and administration** of WALLIX Bastion in a classic architecture, alternating
theory with extensive hands-on labs. It is the prerequisite for **WCE-P**, **WCP-I**
(IDaaS) and **eWCP-P-OT** (OT).

| | |
|---|---|
| **Code** | `WCP-P` (instructor-led) · `eWCP-P` (e-learning) |
| **Level** | Professional (2 of 3) |
| **Product** | WALLIX Bastion + WALLIX Access Manager |
| **Duration** | 3 days (21 hours) |
| **Formats** | Inter-company, intra-company, online/e-learning |
| **Prerequisite** | None formally (natural step after WCA-P) |
| **Exam** | Final MCQ, **70% to pass** |
| **Unlocks** | WCE-P · WCP-I · eWCP-P-OT |

## Target audience

Engineers and technicians of WALLIX end-users and reseller partners who want to master
the **configuration, deployment and administration** of WALLIX Bastion.

## Prerequisites

- **SSH, RDP, proxy concepts, and Linux**; system/network/infrastructure fundamentals.
- **Technical-English** proficiency; **Microsoft Teams** (instructor-led); admin rights
  on laptop for e-learning.
- No prior WALLIX certification formally required, though it is the natural step after
  WCA-P and is itself the prerequisite for WCE-P.

## Objective

Discover and take control of WALLIX Bastion for deployment in a **classical architecture**:
installation, configuration, deployment and administration — alternating theory and
hands-on practice on a LAB platform.

## Curriculum / modules

| # | Module | Topics & labs |
|---|--------|---------------|
| 0 | **Introduction** | WALLIX presentation |
| 1 | **Installing & Handling** | Concept and Installation, Web configuration, System Management · *Lab 1* |
| 2 | **Session Manager** | See breakdown below · *Labs 2.1–2.4* |
| 3 | **Password Manager** | 3.1 Password Checkout (intro, global concept, password visualization — *Lab 3.1*); 3.2 Password Change (Password Change, Break Glass — *Lab 3.2*) |
| 4 | **Approval** | Introduction; Approval workflow for Session Manager; for Password Manager · *Lab 4* |
| 5 | **Audit** | Web audit; Session/Account/Approval/Authentication history; Connection statistics; Session recording parameters; Management of session records · *Lab 5: Session Audit GUI* |
| 6 | **Access Manager** | Introduction, Global concepts, Configuring the Access Manager Part 1 (*Lab 6.1*) & Part 2 (*Lab 6.2: Advanced Configuration*) |
| 7 | **High Availability** | Introduction, Global concepts, HA Solutions, HA in Architecture · *Lab 7: Replication* |
| 8 | **Customer Support Center** | Introduction; Before / Opening / After / Closing a case |

### Module 2 — Session Manager (detailed)

| Sub | Topic |
|-----|-------|
| 2.1 | **Global Concepts** — Explore Session Management; Secondary Connection Methods; Manage Primary Groups; Primary Account Types; Secondary Accounts; Global vs Local Domains; Checkout Policy |
| 2.2 | **Main Configuration** — create/configure primary account & group; target device, account & group; an authorization |
| 2.3 | **User Access** — configure the Bastion User Web Interface; connect via RDP; connect via SSH · *Lab 2.1: RDP & SSH Connections* |
| 2.4 | **Applications** — prerequisites; application creation & publishing; AppDriver concept & configuration · *Lab 2.2: Applications* |
| 2.5 | **Advanced Configuration Part 1** — connection policies & parameters; Session Probe · *Lab 2.3* |
| 2.6 | **Advanced Configuration Part 2** — SSH Startup scenario; external authentication for Bastion; mass import · *Lab 2.4: External Authentication* |

## Lab environment

**6 preconfigured VMs:** Domain Controller (Win 2016), Windows Server 2016, Linux
Server, **2× WALLIX Bastion**, **1× Access Manager** (Azure for instructor-led / OVA for
e-learning). Minimum **4 CPU / i5, 32 GB RAM, 40 GB free**.

## Assessment

Pre-test; oral questions, MCQs and hands-on labs throughout; **final MCQ exam, 70% to
pass** → `WCP-P` / `eWCP-P` certification (digital badge + diploma).

## Concepts worth mastering for the exam

See the [product portfolio — Bastion ACL data model](../00-overview/product-portfolio.md#core-pam-concepts--the-acl-data-model):
*users → user groups → (authorization: Sessions + Secrets rights) → target groups →
targets (resource + account)*; user-mapping modes (account mapping / session account /
interactive login); checkout policies; connection policies & Session Probe.

## Path

⬅️ [WCA-P — Administrator](wca-p-administrator.md) · ➡️ [WCE-P — Expert](wce-p-expert.md)

## Sources

- WALLIX Academy: https://www.wallix.com/support-services/wallix-academy/
- Training catalog 2025–2026 (EN): https://www.wallix.com/wp-content/uploads/2024/04/WALLIX_TRAINING_2025-2026_ENG.pdf
