# eWCP-P-OT — WALLIX Certified Professional – OT (PAM4OT)

Online certification for **WALLIX PAM4OT** — privileged access management purpose-built
for **Operational Technology** (ICS/SCADA, PLCs, HMIs, engineering workstations). The
shortest of the WALLIX certifications (~4 h) and built on top of the PAM/Bastion track.

| | |
|---|---|
| **Code** | `eWCP-P-OT` (catalog) · `eWCP-P OT` (website) · family header "WCP-P-OT" |
| **Level** | Professional |
| **Product** | WALLIX PAM4OT (Bastion packaged for OT) |
| **Duration** | ~4 hours (online) |
| **Format** | Online e-learning |
| **Prerequisite** | **WCP-P (or e-WCP) certification — required** |
| **Exam** | Final MCQ, **70% to pass** |
| **Status** | ✅ Available |

## Target audience

WALLIX end-user engineers, **OT technicians**, and reseller partners.

## Prerequisites

- **Required certification:** **WCP-P** (WALLIX Certified Professional – PAM) or e-WCP.
- System/network/infrastructure fundamentals recommended.
- Technical-English proficiency; admin rights on laptop.

> Assessment uses **demos** rather than a full VM lab — no separate lab hardware list is
> specified in sources.

## Objective

Discover and master the **WALLIX PAM4OT** solution for securing privileged access in
industrial / OT environments.

## Curriculum / modules

| # | Module | Topics |
|---|--------|--------|
| 0 | **Prerequisites** | eWCP-P-OT prerequisites |
| 1 | **Digital Access in OT** | Discover the OT universe (what is OT; main components, equipment & protocols; OT context); security stakes of identity & access |
| 2 | **Advanced Applications** | Typical users & digital access issues; managing third-party access; managing industrial protocols; secure access while preserving service continuity; secure file transfer; secured access to critical assets; trace & audit for incident response and regulatory compliance |
| 3 | **PAM4OT Architectures** | Centralized · Hybrid · Distributed |

## Scope, exam focus & study tips

> *Study guidance **derived** from the published curriculum and the WALLIX product
> documentation — not official WALLIX exam content; question count and weighting are not
> published.*

**Scope — what eWCP-P-OT validates:** that you can position and deploy **WALLIX PAM4OT**
to secure privileged and remote access across **Operational Technology (OT)** environments
— understand the OT world and its identity/access risks, secure third-party/vendor
maintenance access, handle industrial protocols and file transfer **without disrupting
production**, keep an audit trail for compliance, and choose the right PAM4OT architecture.
Because PAM4OT is WALLIX Bastion packaged for OT, this builds directly on
[WCP-P](../pam-bastion/wcp-p-professional.md).

**Likely focus areas (mapped from the modules):**
- The **OT universe** — what OT is; main components, equipment & protocols; the OT context (Module 1).
- The **security stakes of identity & access** in OT (Module 1).
- Securing **third-party / vendor maintenance access** — the flagship OT use case (Module 2).
- Managing **industrial protocols** and **secure file transfer** while **preserving service continuity** (Module 2).
- **Trace & audit** for incident response and regulatory compliance (Module 2).
- The three **PAM4OT architectures**: **Centralized · Hybrid · Distributed** (Module 3).

**Study tips:**
- This builds on **WCP-P** (a required prerequisite) — make sure your Bastion fundamentals
  are solid; revisit the [WCP-P scope](../pam-bastion/wcp-p-professional.md) if rusty.
- Remember **PAM4OT = Bastion for OT**: know how Bastion brokers and records sessions, and
  the OT specifics — **agentless on PLCs**, **industrial-protocol encapsulation in SSH** —
  via the [product portfolio PAM4OT section](../overview/product-portfolio.md#6-wallix-pam4ot--operational-technology-ot-security).
- Learn the OT vocabulary: **ICS, SCADA, PLC, RTU, HMI**, the **IT/OT boundary**, and the
  **Purdue model** (concept). For OT/Purdue fundamentals, the CEH
  [IoT & OT module](../../ceh/domains/18-iot-and-ot-hacking.md) is a good background read.
- Be able to **compare the three architectures** (Centralized / Hybrid / Distributed) and when each fits.
- Know the compliance drivers: **ISA/IEC 62443** and **NIS2**.
- Format is **~4 h online with demos** (not a full VM lab) — focus on concepts, use cases
  and architecture rather than hands-on configuration.

> **Not specified in any WALLIX source** (do not assume): the **number of exam questions**,
> the **exam time limit**, the **certification validity/renewal period**, and the **price**.

## Assessment

Pre-test; MCQs and demos throughout; **final MCQ exam, 70% to pass** → WALLIX Certified
Professional – PAM4OT (`eWCP-P-OT`).

## Technical background

PAM4OT is an **OT-specific packaging of WALLIX Bastion** (sessions flow through the
Bastion), delivered under the **"OT.security by WALLIX"** brand. Key differentiators:
agentless on PLCs/equipment, industrial-protocol encapsulation in SSH tunnels, focus on
third-party maintenance access, and ISA/IEC 62443 alignment.

> 📖 **Full technical deep dive:** **[PAM4OT — Operational Technology](../deep-dives/pam4ot-operational-technology.md)**
> — the OT universe, the Purdue model, how the Bastion engine applies to OT, the three
> architectures, use cases, and ISA/IEC 62443 mapping. Shorter overview in the
> [product portfolio — PAM4OT section](../overview/product-portfolio.md#6-wallix-pam4ot--operational-technology-ot-security).

## Sources

- WALLIX Academy: https://www.wallix.com/support-services/wallix-academy/
- Training catalog 2025–2026 (EN): https://www.wallix.com/wp-content/uploads/2024/04/WALLIX_TRAINING_2025-2026_ENG.pdf
- OT.security by WALLIX: https://www.wallix.com/ot-security/ot-products/ot-pam4ot/
