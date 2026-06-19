# Security & Responsible-Use Policy

This repository is **educational study documentation** — it contains no application code or
service. The "security" considerations here are about **responsible use of the content**
and **factual accuracy**, not software vulnerabilities.

## Responsible / authorized use

Parts of this repo (notably the [CEH hub](ceh/README.md)) explain **offensive** security
concepts. They are written at an **educational, defense-oriented** level and paired with
countermeasures. Any hands-on use of these techniques is legal **only** against systems you
own or are **explicitly authorized in writing** to test. See
[CEH → legal & ethics](ceh/00-overview/legal-and-ethics.md). The maintainers do not condone
unauthorized access.

## Reporting a problem

There's no software to exploit here, so there's nothing to disclose privately. Instead:

- **Factual error, outdated fact, or unsupported claim** → open a
  [content-correction issue](https://github.com/morandeirachema/WallixCerts/issues/new?template=content-correction.md) and include
  the page, the claim, and a citable source. Accuracy is the whole point of this repo
  (see the no-fabrication rule in [CONTRIBUTING.md](CONTRIBUTING.md)).
- **Broken link, diagram, or build problem** → open a regular issue.

## What "secure" means for this repo

- **No secrets** are stored here (no API keys, credentials, or tokens) — and none should
  ever be committed.
- Structural guarantees (no ASCII art, valid Mermaid, a Sources section per page, zero
  broken internal links) are **enforced in CI** by
  [`scripts/check-docs.py`](scripts/check-docs.py) on every push.
