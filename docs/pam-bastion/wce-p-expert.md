# WCE-P — WALLIX Certified Expert – PAM (Bastion)

The **advanced** PAM certification, for large-scale and complex WALLIX Bastion
deployments: Active/Active architecture, automatic provisioning, disaster recovery,
advanced authentication, scripting, proxy tuning, the REST API, and troubleshooting.

| | |
|---|---|
| **Code** | `WCE-P` (instructor-led, sometimes `WCE`) · `eWCE-P` (e-learning) |
| **Level** | Expert (3 of 3) |
| **Product** | WALLIX Bastion + WALLIX Access Manager |
| **Duration** | 2 days (14 hours) |
| **Formats** | Inter-company, intra-company, e-learning |
| **Class size** | 6 trainees max (instructor-led); nominative (e-learning) |
| **Prerequisite** | **WCP-P (or e-WCP) certification — required** + GNU/Linux command line |
| **Exam** | Final MCQ, **70% to pass** |

> **Format availability note:** the WALLIX Academy web page (checked June 2026) marks the
> WCE-P **online** track as *"coming soon"*, while the 2025–2026 catalog PDF fully
> documents an existing **eWCE-P** e-learning track. The sources differ — confirm current
> availability with WALLIX Academy.

## Target audience

Engineers of WALLIX reseller partners and end-users who want to achieve **advanced
deployments** of WALLIX Bastion.

## Prerequisites

- **Required certification (verbatim):** *"WCP-P or e-WCP certified (WALLIX CERTIFIED
  PROFESSIONAL PAM)"* — see [WCP-P](wcp-p-professional.md).
- **GNU/Linux command lines.** *"Scripting knowledge will enable the trainee to handle
  the WALLIX PAM advanced concepts with greater ease."* → work through the
  **[Linux CLI deep dive for WCE-P](../../prerequisites/linux-cli-for-wce-p.md)**.
- Technical-English proficiency; Microsoft Teams (instructor-led); admin rights on
  laptop for e-learning.

## Objective

> *"This 2-day training covers advanced WALLIX PAM deployments, including Active/Active
> architecture, automatic provisioning, and disaster recovery, preparing participants for
> large-scale or complex implementations."* — 2025–2026 catalog
>
> The **eWCE-P** datasheet uses the heading "Training Overview" and the wording "advanced
> WALLIX **Bastion** deployments" — same scope, minor wording difference.

## Curriculum / modules

| # | Module | Topics & labs |
|---|--------|---------------|
| 1 | **Advanced authentication** | 1.1 Global Concepts · 1.2 Bastion: Radius, Kerberos Explicit, X509, Kerberos Transparent, SAML, 2-Factor · 1.3 Access Manager: X509, SAML · *Lab 0 (see note); Lab 1.1: X509; Lab 1.2: Kerberos* |
| 2 | **Advanced Applications** | Global concepts, Reminders, Clusters, **AutoIt** scripting (Write, Compile, Configuration, Secure) · *Lab 2* |
| 3 | **Proxies parameters** | 3.1 Global concepts · 3.2 Common parameters · 3.3 AutoIt (RDP Global params, Sesman, Bastion certificate) · 3.4 SSH (connection policies, global params) · 3.5 Others (TELNET/RLOGIN, **Bastion for OT**, VNC policies & params, RAWTCPIP) · *Lab 3* |
| 4 | **Advanced Password Manager** | Global concepts, Reminders, **WAAPM** (WALLIX Application-to-Application Password Manager), External Vault · *Lab 4* |
| 5 | **WALLIX Bastion REST API** | Global concepts (Methods, Response codes); REST API (Authentication, Resources, Requests) · *Lab 5* |
| 6 | **Troubleshoot** | 6.1 Introduction; 6.2 Bastion Log files; 6.3 Bastion Database; 6.4 Access Manager Log files; 6.5 Access Manager Database; 6.6 Bastion Password Rotation plugins |

> **Lab 0 differs by format:** instructor-led WCE-P Lab 0 = *"Network configuration and
> Bastion 1 configuration"*; eWCE-P Lab 0 = *"Check the configuration of the WALLIX
> Bastion."*

## Lab environment

**5 preconfigured VMs:** Domain Controller (Win 2016), Windows Server 2016, Linux
Server, **2× WALLIX Bastion** (Azure / OVA). Minimum **4 CPU / i5, 32 GB RAM, 40 GB free**.

## Study companion — map each module to a deep dive

| Module | Go deeper |
|--------|-----------|
| 1 Advanced authentication | [Authentication & Access Manager](../../deep-dives/authentication-and-access-manager.md) |
| 2 Advanced Applications | [Session management → applications](../../deep-dives/session-management.md) |
| 3 Proxies parameters | [Session management](../../deep-dives/session-management.md) · [architecture](../../deep-dives/bastion-architecture.md) |
| 4 Advanced Password Manager (WAAPM) | [Secrets & password management](../../deep-dives/secrets-and-password-management.md) |
| 5 WALLIX Bastion REST API | [REST API & automation](../../deep-dives/rest-api-and-automation.md) |
| 6 Troubleshoot | [Troubleshooting & logs](../../deep-dives/troubleshooting-and-logs.md) |
| (Active/Active, DRP) | [High availability & DR](../../deep-dives/high-availability-and-dr.md) |

Self-test: [practice questions](../../exam-prep/practice-questions.md).

## Scope, exam focus & study tips

> *Study guidance **derived** from the published curriculum and product documentation —
> not official WALLIX exam content; question count and weighting are not published.*

**Scope — what WCE-P validates:** that you can deliver **advanced, large-scale or
complex** Bastion deployments — advanced authentication on both Bastion and Access
Manager, application scripting, proxy tuning, application-to-application secrets, the REST
API, and troubleshooting, plus Active/Active architecture, automatic provisioning and
disaster recovery.

**Likely focus areas (mapped from the modules):**
- The **authentication matrix** — RADIUS, Kerberos **explicit vs transparent**, X.509, SAML, 2-factor — and which methods apply to Bastion vs Access Manager (Module 1).
- **AutoIt** application scripting: write / compile / configure / secure (Module 2).
- **Proxy parameters** per protocol — RDP, SSH, VNC, TELNET/RLOGIN, **Bastion for OT**, RAWTCPIP (Module 3).
- **WAAPM** (application-to-application) and **external vaults** (Module 4).
- **REST API** — authentication, resources, requests, methods and response codes (Module 5).
- **Troubleshooting** — Bastion/Access Manager **log files and databases**, password-rotation plugins (Module 6).

**Study tips:**
- You need genuine **GNU/Linux command-line** comfort — this is a stated prerequisite.
  Work through the **[Linux CLI deep dive for WCE-P](../../prerequisites/linux-cli-for-wce-p.md)** first.
- Know the auth methods **cold**, especially **Kerberos explicit vs transparent** and which
  leg each covers — see [Authentication & Access Manager](../../deep-dives/authentication-and-access-manager.md).
- Be able to make a **REST API** call (authenticate with an API key, read a resource) — see
  [REST API & automation](../../deep-dives/rest-api-and-automation.md).
- Know **where the logs and databases live** for both products — see
  [Troubleshooting & logs](../../deep-dives/troubleshooting-and-logs.md).
- Understand **WAAPM vs external vault**, and **Active/Active + disaster recovery** — see
  [HA & DR](../../deep-dives/high-availability-and-dr.md).
- Basic **scripting** (AutoIt for applications, shell for operations) makes Modules 2–3 and troubleshooting much easier.

## Assessment

Pre-test; **final MCQ exam, 70% to pass** → `WCE-P` / `eWCE-P` certification (digital
badge + diploma). Continuous assessment during the course:
- **Instructor-led (WCE-P):** oral questions, MCQs, and hands-on labs.
- **E-learning (eWCE-P):** MCQs and hands-on labs (no oral questions).

> **Not specified in any WALLIX source:** the **number of exam questions**, the **exam
> time limit**, the **certification validity/renewal period**, and the **price**. Confirm
> with WALLIX Academy (`academy@wallix.com`).

## Path

⬅️ [WCP-P — Professional](wcp-p-professional.md) *(required prerequisite)*

## Sources

- WALLIX Academy: https://www.wallix.com/support-services/wallix-academy/
- Training catalog 2025–2026 (EN) — primary, retrieved full (35 pp.): https://www.wallix.com/wp-content/uploads/2024/04/WALLIX_TRAINING_2025-2026_ENG.pdf
