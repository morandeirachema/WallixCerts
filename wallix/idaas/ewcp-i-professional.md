# eWCP-I / WCP-I — WALLIX Certified Professional – IDaaS

Online certification for **WALLIX One IDaaS** (the Identity-as-a-Service platform
historically branded **Trustelem**): cloud SSO, MFA and identity federation. Builds on
the PAM/Bastion track.

| | |
|---|---|
| **Code** | `eWCP-I` (catalog) · `WCP-I` (website) |
| **Level** | Professional |
| **Product** | WALLIX One IDaaS / Trustelem (incl. WALLIX Authenticator) |
| **Duration** | ~7 hours (online) |
| **Format** | Online e-learning |
| **Prerequisite** | **WCP-P (or e-WCP) certification — required** |
| **Exam** | Final MCQ, **70% to pass** |
| **Status** | ✅ Available |

## Target audience

Engineers and technicians of WALLIX end-users and reseller partners.

## Prerequisites

- **Required certification:** **WCP-P** (WALLIX Certified Professional – PAM Bastion) or e-WCP.
- Technical knowledge of **Active Directory** objects and Microsoft environments.
- Technical-English proficiency; admin rights on laptop.

## Objective

Introduce WALLIX One IDaaS and its key concepts/functionalities for a **standard
deployment**.

## Curriculum / modules

| # | Module | Topics |
|---|--------|--------|
| 1 | **Product Presentation** | Identity-as-a-Service; LDAP/Radius; users from Azure AD/GSuite/AD; applications; workflow; access rules; second factors; Integrated Windows Authentication; certificate auth; self-service password reset; delegated administration; API |
| 2 | **Kick-off & Planning** | Client needs; planning; prerequisites |
| 3 | **Users Management** | Production config; AD user sync; AD users IWA; local user creation; delegated admin; access rules; 2nd factors; SSPR · *Labs 1–5: user management, IWA, SSPR, SAML app, SAML app with LDAP connector, OpenID Connect app* |
| 4 | **Product Launch** | 7-step rollout: directories/groups/admin accounts; factors/campaigns; SSO LDAP/Radius; IP/access rules; IWA/certificate/SSPR/delegated admin; communication plan; local users/enable campaign; follow-up |

## Lab environment

Labs via **OVA**. Minimum **4 CPU / i5, 32 GB RAM, 40 GB free**. **2 preconfigured VMs**
(Domain Controller Win 2016, Linux Server) + an **IDaaS tenant**. The course creates a
"Trustelem subscription," confirming the Trustelem lineage.

## Scope, exam focus & study tips

> *Study guidance **derived** from the published curriculum and product documentation —
> not official WALLIX exam content; question count and weighting are not published.*

**Scope — what eWCP-I validates:** that you can introduce, configure and run **WALLIX One
IDaaS / Trustelem** for a **standard deployment** — connect identity sources, build SSO
applications (SAML / OIDC), enable second factors and SSPR, write access rules, and
execute the 7-step product launch.

**Likely focus areas (mapped from the modules):**
- **IDaaS concepts** and the difference between **SSO** (SAML 2.0 / OIDC / OAuth 2.0) and
  **non-federated** auth via **LDAP / RADIUS** (Module 1).
- **AD user sync and IWA** via the connectors, plus **local user creation** and
  **delegated administration** (Modules 1, 3).
- **Second factors** — WALLIX Authenticator (push/TOTP), TOTP, FIDO2/WebAuthn security
  keys, SMS/email OTP — and **which factors cannot be used over LDAP/RADIUS** (Modules 1, 3).
- **Access rules** with **internal vs external IP zones** and rule precedence (Modules 1, 3, 4).
- **Self-Service Password Reset (SSPR)**, **certificate auth**, and the **API** (Module 1).
- The labs map straight to skills: **IWA, SSPR, a SAML app, a SAML app with the LDAP
  connector, and an OpenID Connect app** (Module 3 Labs 1–5).
- The **7-step rollout** (directories/groups/admin accounts → factors/campaigns → SSO
  LDAP/Radius → IP/access rules → IWA/certificate/SSPR/delegated admin → communication →
  go-live/follow-up) in Module 4.

**Study tips:**
- Read the technical companion first: the
  [WALLIX One IDaaS / Trustelem deep dive](../deep-dives/idaas-trustelem.md) — it
  expands every module topic with sourced detail and Mermaid flows.
- Be able to **draw the SP-initiated SAML 2.0 SSO flow** end to end (request → IdP auth →
  MFA → signed assertion to ACS).
- Memorize the **five MFA factors** and the rule that **FIDO2 security keys do not work
  over LDAP/RADIUS** (push/TOTP do), and that **strong auth = two *different kinds* of
  factors**.
- Know the **two connectors** — **ADConnect** (AD sync/auth, stores no AD passwords) and
  **Trustelem Connect** (local LDAP/RADIUS + SCIM relay) — both **outbound 443
  WebSocket**, no inbound firewall opening.
- Understand **SCIM 2.0** provisioning (create/update on grant, deactivate on revoke,
  ~5-min push) and **Access Rule precedence** (user > group > everyone; most restrictive
  wins).

## Assessment

Pre-test; MCQs and hands-on labs throughout; **final MCQ exam, 70% to pass** → WALLIX
Certified Professional – IDaaS (`eWCP-I`).

> **Not specified in any WALLIX source:** the **number of exam questions**, the **exam
> time limit**, the **certification validity/renewal** period, and the **price**. Confirm
> with WALLIX Academy (`academy@wallix.com`).

## Technical background

WALLIX One IDaaS = European IDaaS delivering **SSO (SAML 2.0 / OIDC / OAuth 2.0)**, **MFA**
(WALLIX Authenticator push/TOTP, FIDO/WebAuthn, SMS/email OTP), **LDAP/RADIUS** for
non-federated apps, **SCIM 2.0** provisioning, and AD/Azure AD integration via the
ADConnect / Trustelem Connect lightweight connectors. See the
[product portfolio — Trustelem section](../overview/product-portfolio.md#3-wallix-trustelem--idaas-sso--mfa--identity-federation).

> **Note:** In the 2023 catalog this was a 1-day in-person/LAB course titled
> "IDaaS – Trustelem" (`WCP-I`). The 2025–2026 version is the modernized **online**
> (`eWCP-I`) replacement.

## Sources

- WALLIX Academy: https://www.wallix.com/support-services/wallix-academy/
- Training catalog 2025–2026 (EN): https://www.wallix.com/wp-content/uploads/2024/04/WALLIX_TRAINING_2025-2026_ENG.pdf
- WALLIX IDaaS product page: https://www.wallix.com/products/idaas/
