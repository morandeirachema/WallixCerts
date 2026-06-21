# Contributing

This repo is an **unofficial, source-grounded study hub** for WALLIX and Privileged
Access Management (PAM). Contributions are welcome — but accuracy is the whole point of
the project, so please follow these rules.

## The one hard rule: no fabrication

**Never invent facts, figures, dates, URLs, product behaviors, or exam questions
presented as real.** Every factual claim must either:

- trace to a cited official source (WALLIX docs, standards bodies, vendor pages), or
- be clearly labeled as a pedagogical example, estimate, or "suggested" value.

If you don't know something, write **"not specified in sources"** — do not guess. Flag
any uncertainty inline. Practice questions must carry the disclaimer that they are
unofficial study aids, not real exam content.

## Sourcing

- Prefer **official WALLIX documentation** for product specifics: the
  [training catalog](https://www.wallix.com/wp-content/uploads/2024/04/WALLIX_TRAINING_2025-2026_ENG.pdf),
  `wallix.com`, `pam.wallix.one`, `trustelem-doc.wallix.com`. Use reputable sources
  (NIST, MITRE ATT&CK, RFCs, ENISA, standards bodies, analyst press) for general topics.
- **Every page ends with a `## Sources` section** listing the URLs actually used.
- When citing a WALLIX PDF whose served version differs from its URL label, note the
  served version (e.g. Bastion Admin Guide served as v12.3.2).

## Page conventions

- Start with an `# H1` title, a 1–2 sentence intro, and a short "Learning objectives" or
  key-points list where it fits.
- Lean into the three things this repo is built around: **concepts** explained from first
  principles, **flows** (diagrams — see the Diagrams rule below), and **acronyms** (expand
  every acronym on first use, e.g. "Privileged Access Management (PAM)").
- Use tables, lists, and fenced code blocks. Write **dates absolute** (e.g. `2026-06-17`).
- **Cross-link with relative paths.** Top-level folders are siblings, so use
  `../<folder>/<file>.md`. Don't duplicate the product portfolio — link to it and go deeper.
- No author or tool attribution anywhere in files **or commit messages**.

### Diagrams — always Mermaid, never ASCII art

Author **every diagram as a GitHub-rendered [Mermaid](https://mermaid.js.org/) block**
(` ```mermaid `). Do **not** use ASCII / box-drawing art — the whole repo was converted to
Mermaid and new diagrams must match. Pick the fitting type:

| Use for | Mermaid type |
|---------|--------------|
| Processes, architecture, topologies, decision trees | `flowchart TD` / `LR` |
| Protocol / message exchanges between parties | `sequenceDiagram` |
| Data models / entity relationships | `erDiagram` |
| 2×2 analyst positioning | `quadrantChart` |
| Time-phased roadmaps | `timeline` |

Syntax rules so it renders on GitHub: quote labels containing spaces/special characters
(`id["Text (parens), a/b"]`), use `<br/>` for line breaks, keep node IDs alphanumeric, and
never use reserved words (`end`, `graph`, `subgraph`) as IDs. Leave genuine
code/CLI/config blocks as code. Translate faithfully — never invent steps or facts.

**Boxes must fit their text.** Mermaid sizes a node box to its widest line, so keep each
node-label line short (≈ ≤ 40 characters) and **wrap long labels with `<br/>`** into a few
short lines. Run **`python scripts/wrap-mermaid-labels.py`** to auto-wrap them; the quality
gate (`scripts/check-docs.py`) fails on over-wide flowchart labels.

## Adding a new page

1. Put it in the right section folder. WALLIX material goes under `wallix/`
   (`wallix/overview/`, `wallix/pam-bastion/`, `wallix/deep-dives/`, `wallix/labs/`,
   `wallix/exam-prep/`, `wallix/career/`); shared fundamentals stay at the root
   (`foundations/`, `prerequisites/`, `protocols/`, `reference/`); other certs are their
   own top-level hubs (`ceh/`, `security-plus/`, `cysa-plus/`, `pentest-plus/`, `oscp/`, `pnpt/`).
2. Add a row for it in that folder's `README.md` index.
3. If it's a new certification, follow the structure of
   `wallix/pam-bastion/wcp-p-professional.md` and add it to the matrix in the root `README.md`.
4. Add any new authoritative URLs to `reference/sources.md`.

## Periodic verification checklist

Some facts drift over time. Re-check these against primary sources before relying on them,
and update the affected pages + their `## Sources`:

- [ ] **WALLIX training catalog year** — currently the 2025–2026 catalog. Check for a newer edition.
- [ ] **Certification validity period & exam question counts** — *not specified in sources*; check if WALLIX ever publishes them.
- [ ] **Website-vs-catalog code mismatch** (`WCP-G` vs `eWCP-G`, etc.) — confirm it still exists.
- [ ] **WCA-G (IAG Administrator)** — listed "coming soon"; check if it has launched.
- [ ] **Analyst placements (change yearly):** Gartner Magic Quadrant for PAM and
      KuppingerCole Leadership Compass for PAM — update WALLIX's position and the year.
- [ ] **WALLIX product doc versions** referenced in `wallix/deep-dives/` (Bastion 12.3.2, Access
      Manager 5.2.4.0, Deployment 12.0.2) — note newer served versions.
- [ ] **WALLIX product security certifications** — ANSSI CSPN / BSI BSZ versions and dates.
- [ ] **Adjacent certifications** flagged as time-sensitive in `wallix/career/`: Microsoft
      **AZ-500** (retirement date), **(ISC)² CC** (outline refresh), and the exact program
      names for CyberArk / Delinea / One Identity — verify on each provider's site.

## License & disclaimer

By contributing you agree to license your contribution under the repository's
[LICENSE](LICENSE). This project is **not affiliated with or endorsed by WALLIX**;
"WALLIX", "Bastion", "Trustelem", "BestSafe", and related names are trademarks of their
respective owners and are used here for identification and educational purposes only.
