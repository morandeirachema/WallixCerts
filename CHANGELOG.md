# Changelog

Notable changes to this study repo. Dates are when the work landed on `main`.
This is a documentation repo, so "changes" are content additions and corrections.

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
- **Cross-hub learning roadmap** (`learning-roadmap.md`) connecting foundations → Security+
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
