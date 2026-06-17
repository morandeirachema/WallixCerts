# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A **documentation-only repository** (pure Markdown, no source code, no build/test/lint
tooling) — a **self-study hub** for a sysadmin moving into cybersecurity and specializing
in Privileged Access Management (PAM) with the WALLIX suite and its
[WALLIX Academy](https://www.wallix.com/support-services/wallix-academy/) certifications.
There is nothing to build or run — work is editing `.md` files; validation is review/
preview of Markdown only.

Two layers of content:
- **Reference docs** under `docs/` — the certification framework and the WALLIX product
  portfolio (this layout mirrors WALLIX's certification taxonomy; see below).
- **Learning-path sections** as sibling top-level folders, meant to be read in order:
  `foundations/` (PAM concepts) → `prerequisites/` (Linux, AD, networking, crypto) →
  `docs/` (products & certs) → `deep-dives/` (Bastion internals) → `labs/` →
  `exam-prep/` → `career/`, plus `reference/` (glossary, acronyms, compliance, sources).
  Each folder has a `README.md` index; the root `README.md` is the learning-path hub.
  Cross-folder links are relative siblings: `../<folder>/<file>.md`.

## Organizing principle: the certification taxonomy

The directory layout deliberately mirrors WALLIX's own certification taxonomy, so you
must understand the taxonomy to know where content belongs:

- **Three levels** build on each other: `WCA` (Administrator) → `WCP` (Professional) →
  `WCE` (Expert).
- **Code format** is `WC{level}-{track}`; an `e` prefix means the e-learning variant
  (e.g. `eWCP-P`). Track suffixes: `P` = PAM/Bastion, `G` = IAG, `I` = IDaaS,
  `P-OT` = OT.
- Each **track** is a folder under `docs/` (`pam-bastion/`, `iag/`, `idaas/`,
  `ot-pam4ot/`); each **certification** is one file inside it. `docs/00-overview/` holds
  the cross-cutting framework doc and the product-portfolio technical reference.

Known wrinkle to preserve: the WALLIX **website and the catalog use inconsistent codes**
(e.g. `WCP-G` vs `eWCP-G`, `WCP-I` vs `eWCP-I`). Document both rather than "correcting"
one.

## Per-certification doc convention

When adding or editing a certification doc, follow the established structure (see
`docs/pam-bastion/wcp-p-professional.md` as the canonical example): a title + summary
table (code / level / product / duration / format / prerequisite / exam / status),
then **Target audience → Prerequisites → Objective → Curriculum/modules (as a table) →
Lab environment → Assessment → Path/links → Sources**. Curricula are transcribed module-
by-module from the catalog, including lab names.

## Sourcing discipline (most important)

This is a factual reference, so accuracy rules over completeness. **NO FABRICATION is a
hard rule** (the repo owner insists): never invent facts, figures, dates, URLs, product
behaviors, or exam questions presented as real. Every claim traces to a cited source or
is clearly labeled as a pedagogical example/estimate.

- The **primary source** is the official training catalog
  (`WALLIX_TRAINING_2025-2026_ENG.pdf`); the live Academy page and product docs are
  secondary. Every doc ends with a **Sources** list of the URLs actually used.
- Where a fact is unknown, write **"not specified in sources"** — never invent it.
  (Notably, WALLIX does not publish exam question counts or certification validity
  periods; keep these marked as unspecified.)
- **Flag uncertainties inline.** The product portfolio's "Key uncertainties" section is
  the model. Established corrections to preserve: inWebo is a *technology partner* (not
  acquired); WALLIX IAG = the acquired *Kleverware* product; PAM4OT is *Bastion packaged
  for OT*, not a separate engine; Bastion has ANSSI CSPN + BSI BSZ but no confirmed
  Common Criteria EAL.
- When a doc cites a WALLIX PDF whose served version differs from its URL label, note the
  served version (the portfolio doc does this for Bastion 12.3.2 and Access Manager
  5.2.4.0).

## Scope decision to respect

The **EPM / `WCP-E` (BestSafe) certification is intentionally excluded** — it was
"FUTURE" in the 2023 catalog and absent from the current one. BestSafe remains in
`docs/00-overview/product-portfolio.md` as a current *product*, but do not re-add it as a
certification track unless WALLIX publishes one.

## Conventions

- **Diagrams are always Mermaid, never ASCII art.** Author every diagram as a
  GitHub-rendered ` ```mermaid ` block (`flowchart`, `sequenceDiagram`, `erDiagram`,
  `quadrantChart`, `timeline`). Quote labels with special chars (`id["a/b (c)"]`), use
  `<br/>` for line breaks, keep node IDs alphanumeric, and avoid reserved words (`end`,
  `graph`, `subgraph`) as IDs. Leave genuine code/CLI/config blocks as code. The repo was
  fully converted to Mermaid — keep it that way. See CONTRIBUTING.md for the type table.
- **Cross-link with relative paths** between docs; link into the product portfolio using
  its section anchors (e.g. `product-portfolio.md#3-wallix-trustelem-...`).
- **Dates** are written absolute (e.g. "2026-06-17"), not relative.
- **Commits:** do not include any author/tool attribution lines (no "Co-Authored-By",
  no Claude references) — repo-wide convention.
