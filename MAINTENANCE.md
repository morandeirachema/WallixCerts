# Maintenance & verification

How this repo stays accurate over time.

## Automated checks (CI)

| Workflow | When | What it enforces |
|----------|------|------------------|
| [`quality.yml`](.github/workflows/quality.yml) | every push / PR | No ASCII art · balanced code fences · valid Mermaid (and no reserved-word node IDs) · a `## Sources` section on every content page · **zero broken internal links/anchors** — via [`scripts/check-docs.py`](scripts/check-docs.py) |
| [`external-links.yml`](.github/workflows/external-links.yml) | weekly + on demand | External URL rot (RFCs, vendor docs) — non-blocking |
| [`docs.yml`](.github/workflows/docs.yml) | every push to `main` | Builds & deploys the MkDocs site |

Run the gate locally before committing:

```bash
python scripts/check-docs.py
```

## Manual re-verification

Some facts drift (cert exam specs, product versions, analyst placements, retirement
dates). The per-topic re-verification checklist lives in
[`CONTRIBUTING.md`](CONTRIBUTING.md#periodic-verification-checklist). Volatile items are
marked **"verify on \<provider\>"** or **"not specified in sources"** inline rather than
asserted.

## Verification status

- **Full source verification pass:** 2026-06-18 — audit-flagged WALLIX specifics
  re-checked against the official guides; all confirmed. See [`CHANGELOG.md`](CHANGELOG.md).
- Last structural check (links/Mermaid/ASCII/Sources): enforced continuously by CI.
