# Changelog

Notable changes to this study repo. Dates are when the work landed on `main`.
This is a documentation repo, so "changes" are content additions and corrections.

## 2026-06-22

### Changed — folder reorganization
- **Grouped every certification hub under one top-level `certs/` folder**:
  `certs/wallix/`, `certs/ceh/`, `certs/security-plus/`, `certs/cysa-plus/`,
  `certs/pentest-plus/`, `certs/oscp/`, `certs/pnpt/`, `certs/adjacent-certs/`. Added
  `certs/README.md` indexing them.
- The top level is now minimal: `certs/` + the shared knowledge it draws on
  (`foundations/`, `prerequisites/`, `protocols/`, `reference/`, `learning/`,
  `attack-to-defense-matrix.md`).
- All affected cross-links recomputed via the path-aware migration; nav, root README,
  `CLAUDE.md`, and `CONTRIBUTING.md` updated. Gate: 175 files, 0 broken links.

## 2026-06-21 (later)

### Changed — folder reorganization
- **Consolidated all WALLIX-specific material under a single top-level `wallix/` folder**:
  `wallix/overview/` (was `docs/00-overview/`), `wallix/pam-bastion/` · `iag/` · `idaas/` ·
  `ot-pam4ot/` (was under `docs/`), and `wallix/deep-dives/`, `wallix/labs/`,
  `wallix/exam-prep/`, `wallix/career/`. Added `wallix/README.md` as the WALLIX hub index.
- **Shared fundamentals stay at the repo root** (`foundations/`, `prerequisites/`,
  `protocols/`, `reference/`, `learning/`) since every cert hub uses them; the other cert
  hubs remain their own top-level folders.
- All ~738 affected cross-links were recomputed automatically; the curated nav, root README
  (layout diagram + WALLIX section), `CLAUDE.md`, and `CONTRIBUTING.md` were updated.

## 2026-06-21

### Added
- **Four more full certification hubs** (each like the Security+/CEH hubs):
  - **CompTIA CySA+** (`cysa-plus/`, CS0-003) — blue-team / SOC analyst: 4 domains, exam prep, glossary.
  - **CompTIA PenTest+** (`pentest-plus/`, PT0-003) — vendor-neutral pentesting: 5 domains, exam prep, glossary.
  - **OSCP / OSCP+** (`oscp/`, OffSec PEN-200) — hands-on offensive: 6 skill areas, exam structure, study plan.
  - **PNPT** (`pnpt/`, TCM Security) — practical engagement + live debrief: 5 engagement phases, study plan.
- Offensive hubs (PenTest+, OSCP, PNPT) carry the same authorized-use / defensive framing as
  CEH; their attack pages cross-link the [attack → defense matrix](attack-to-defense-matrix.md)
  and the WALLIX/PAM defenses.
- The `adjacent-certs/` overviews for Security+/OSCP/PNPT now point to their full hubs.
- Wired all hubs into the curated nav, root README ("Start here" + a cert-hub table), and roadmap.

## 2026-06-20

### Added
- **CompTIA Security+ (SY0-701) full study hub** (`security-plus/`) — a third full hub
  alongside CEH and WALLIX/PAM: overview + exam & objectives, all **5 domains** taught to
  the official objectives (general concepts · threats/vulns · architecture · operations ·
  program management), exam prep (study plan, 52 practice questions, cheat sheet), and a
  long acronyms + glossary reference. Vendor-neutral, source-cited (CompTIA + NIST).
- The one-page `adjacent-certs/security-plus.md` now points to the full hub.
- Wired into the curated nav, root README, and learning roadmap.

## 2026-06-19

### Added
- **Protocol mechanism deep dives** (`protocols/`): Kerberos, Active Directory, LDAP,
  RADIUS, TLS, SSH, SAML, and OIDC/OAuth 2.0 — message flows, what's signed/encrypted and
  how, grounded in the RFCs with Mermaid sequence diagrams.
- **[Attack → Defense matrix](attack-to-defense-matrix.md)** — maps CEH attack techniques
  (with MITRE ATT&CK IDs) to the PAM/WALLIX controls that mitigate them; bridges the hubs.
- **CI quality gate** — `scripts/check-docs.py` + `.github/workflows/quality.yml` enforce
  no ASCII art, valid Mermaid, a Sources section per page, and zero broken internal
  links/anchors on every push; `external-links.yml` checks URL rot weekly.
- **Curated MkDocs navigation**, `SECURITY.md`, issue/PR templates, and `MAINTENANCE.md`.
- Cross-links between the WALLIX and CEH glossaries/acronyms.

### Changed
- `protocols/` index, the root README, and the learning roadmap updated for the new pages.

## 2026-06-18

### Added
- **Adjacent-certification overviews** (`adjacent-certs/`): CompTIA Security+, OSCP/OSCP+,
  PNPT, CISSP, and cloud security (Azure AZ-500 / AWS Security) — concise, provider-cited
  orientation pages.
- **WALLIX product deep dives** (`deep-dives/`): WALLIX One IDaaS / Trustelem, WALLIX IAG
  (Identity & Access Governance), WALLIX BestSafe / EPM, and WALLIX One (SaaS) &
  integrations — rounding out the product family beyond Bastion.
- **PAM4OT (Operational Technology) deep dive** and the **OT certification** scope/tips.
- **CEH topics**: "AI in ethical hacking" (the v13 "CEH AI" theme + OWASP LLM Top 10) and
  "Engagement methodology & reporting" (PTES / NIST SP 800-115 / OSSTMM, the report).
- **Cross-hub learning roadmap** (`learning/roadmap.md`) connecting foundations → Security+
  → CEH/PAM → OSCP/cloud → CISSP.
- **Scope, exam-focus & study-tips** sections on the IAG and IDaaS cert docs (matching PAM/OT).
- **MkDocs Material** site config (`mkdocs.yml`) + a GitHub Pages deploy workflow, and
  **GitHub repo topics** for discoverability. *(The site config is provided as a starting
  point — verify with a local `mkdocs serve` before relying on Pages.)*

### Changed / verified
- **No-fabrication verification pass**: re-checked the audit-flagged precise WALLIX values
  (Break-Glass time, session/SAML timeouts, plugin versions, JVM heap, CSPN build,
  Kerberos default-on version) against the official guides — all confirmed verbatim. Reworded
  the one true placeholder (Kerberos-Password "v12.X").
- Fixed broken internal anchor links; repo now passes a 0-broken-link / 0-broken-anchor check.
- Refreshed outdated specifics (VMware desktop licensing) and softened/attributed a few
  claims (OWASP Mobile Top 10 edition, "leading cloud breach cause", non-human-account ratio).

## 2026-06-17

### Added
- **CEH v13 study hub** (`ceh/`): 20 module pages, the 5 phases, exam & eligibility, legal &
  ethics, tools, labs, exam prep, career, glossary & acronyms — defense-oriented, no
  weaponized content.
- **All diagrams converted to Mermaid** (no ASCII art); root README redesigned; the
  Mermaid-only convention documented in `CLAUDE.md` and `CONTRIBUTING.md`.
- **WALLIX/PAM study hub**: foundations, prerequisites, product portfolio, the WCA/WCP/WCE
  certification tracks, Bastion deep dives, labs, exam prep, career, and reference.
- `CLAUDE.md`, `CONTRIBUTING.md` (with the no-fabrication rule + verification checklist),
  and an MIT `LICENSE`.

### Principles (apply throughout)
- **No fabrication** — every factual claim is cited or marked "not specified in sources".
- **Mermaid-only diagrams** — never ASCII art.
- Each page ends with a **Sources** section.
