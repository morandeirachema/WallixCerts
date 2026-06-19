#!/usr/bin/env bash
# Assemble the repo's root-level Markdown into a MkDocs docs_dir (./site-src).
# Needed because the content lives at the repo root, while MkDocs 1.6 requires
# docs_dir to be a child directory of mkdocs.yml.
#
# Usage:
#   bash scripts/build-site.sh        # populate ./site-src
#   mkdocs build                      # or: mkdocs serve  /  mkdocs gh-deploy --force
set -euo pipefail
cd "$(dirname "$0")/.."

rm -rf site-src
mkdir -p site-src
rsync -a \
  --exclude '.git' \
  --exclude '.github' \
  --exclude '.claude' \
  --exclude 'site' \
  --exclude 'site-src' \
  --exclude 'scripts' \
  --exclude 'mkdocs.yml' \
  ./ site-src/

echo "Populated ./site-src — now run: mkdocs build  (or mkdocs serve / mkdocs gh-deploy --force)"
