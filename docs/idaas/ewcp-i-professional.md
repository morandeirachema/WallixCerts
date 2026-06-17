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

## Assessment

Pre-test; MCQs and hands-on labs throughout; **final MCQ exam, 70% to pass** → WALLIX
Certified Professional – IDaaS (`eWCP-I`).

## Technical background

WALLIX One IDaaS = European IDaaS delivering **SSO (SAML 2.0 / OIDC / OAuth 2.0)**, **MFA**
(WALLIX Authenticator push/TOTP, FIDO/WebAuthn, SMS/email OTP), **LDAP/RADIUS** for
non-federated apps, **SCIM 2.0** provisioning, and AD/Azure AD integration via the
ADConnect / Trustelem Connect lightweight connectors. See the
[product portfolio — Trustelem section](../00-overview/product-portfolio.md#3-wallix-trustelem--idaas-sso--mfa--identity-federation).

> **Note:** In the 2023 catalog this was a 1-day in-person/LAB course titled
> "IDaaS – Trustelem" (`WCP-I`). The 2025–2026 version is the modernized **online**
> (`eWCP-I`) replacement.

## Sources

- WALLIX Academy: https://www.wallix.com/support-services/wallix-academy/
- Training catalog 2025–2026 (EN): https://www.wallix.com/wp-content/uploads/2024/04/WALLIX_TRAINING_2025-2026_ENG.pdf
- WALLIX IDaaS product page: https://www.wallix.com/products/idaas/
