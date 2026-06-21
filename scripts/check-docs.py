#!/usr/bin/env python3
"""Quality gate for the repo's Markdown.

Checks, across all *.md (excluding .git / site / site-src):
  - no ASCII-art diagrams (box-drawing or +--/--+);
  - balanced ``` code fences;
  - every ```mermaid block starts with a valid diagram type and uses no
    reserved word (end/graph/subgraph) as a node id;
  - flowchart node-label lines fit the box (no over-wide single line — wrap
    long labels with <br/>; run scripts/wrap-mermaid-labels.py to fix);
  - every content page has a "## Sources" section (READMEs and meta files exempt);
  - no broken internal file links or heading anchors (GitHub slug rules).

Exits non-zero (and lists the problems) if anything fails. Run from anywhere:
    python scripts/check-docs.py
"""
import os
import re
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

SKIP = ('.git/', 'site/', 'site-src/', 'node_modules/')
MD = [p for p in glob.glob('**/*.md', recursive=True)
      if not any(s in (p + '/') for s in SKIP)]

MERMAID_TYPES = (
    'flowchart', 'graph', 'sequenceDiagram', 'erDiagram', 'classDiagram',
    'stateDiagram', 'stateDiagram-v2', 'quadrantChart', 'timeline', 'gantt',
    'mindmap', 'journey', 'pie',
)
SOURCES_EXEMPT = {
    'README.md', 'CLAUDE.md', 'CONTRIBUTING.md', 'CHANGELOG.md',
    'SECURITY.md', 'LICENSE', 'MAINTENANCE.md',
}

ASCII_RE = re.compile(r'[─-╿▀-▟]|\+--|--\+')
LINK_RE = re.compile(r'(?<!\!)\[[^\]]*\]\(([^)]+)\)')
HEADING_RE = re.compile(r'^(#{1,6})\s+(.*)')


def slugs(path):
    """Heading anchor slugs, computed exactly like GitHub (github-slugger):
    lowercase, strip HTML, remove all but [word, space, hyphen], spaces -> '-',
    NO trimming of leading/trailing hyphens (so emoji headings keep their leading
    '-'), and append -1/-2 for duplicates. Matching is exact — no leniency — so a
    link that would 404 on GitHub fails here too."""
    out, counts = [], {}
    for line in open(path, encoding='utf-8'):
        m = HEADING_RE.match(line)
        if not m:
            continue
        text = re.sub(r'#+\s*$', '', m.group(2).strip()).strip()
        s = re.sub(r'[^\w\- ]', '', re.sub(r'<[^>]+>', '', text.lower())).replace(' ', '-')
        if s in counts:
            counts[s] += 1
            out.append(f"{s}-{counts[s]}")
        else:
            counts[s] = 0
            out.append(s)
    return set(out)


SLUGMAP = {os.path.normpath(f): slugs(f) for f in MD}
issues = []

for f in MD:
    text = open(f, encoding='utf-8').read()
    lines = text.splitlines()

    for i, line in enumerate(lines, 1):
        if ASCII_RE.search(line):
            issues.append(f"ASCII art: {f}:{i}")
            break

    if len(re.findall(r'(?m)^```', text)) % 2:
        issues.append(f"Unbalanced ``` fences: {f}")

    for m in re.finditer(r'```mermaid\n(.*?)```', text, re.S):
        body = m.group(1)
        first = next((x.strip() for x in body.splitlines() if x.strip()), '')
        if not first.startswith(MERMAID_TYPES):
            issues.append(f"Bad Mermaid header: {f}: {first[:40]!r}")
        for line in body.splitlines():
            if re.match(r'\s*(end|subgraph|graph)\s*[\[\(]', line):
                issues.append(f"Reserved word as Mermaid node id: {f}: {line.strip()[:40]}")
        # Flowchart node boxes should fit their text: no over-wide single label line.
        if first.startswith(('flowchart', 'graph')):
            for _opener, label in re.findall(r'([\[({]+)"([^"]*)"', body):
                for seg in label.split('<br/>'):
                    if len(seg) > 44 and ' ' in seg.strip():
                        issues.append(f"Over-wide Mermaid label (wrap with <br/>): {f}: {seg[:48]!r}")

    if os.path.basename(f) not in SOURCES_EXEMPT and not re.search(r'(?im)^#+\s*sources\b', text):
        issues.append(f"Missing Sources section: {f}")

    d = os.path.dirname(f)
    for ln, line in enumerate(lines, 1):
        for tgt in LINK_RE.findall(line):
            tgt = tgt.strip().split(' ')[0]
            if tgt.startswith(('http://', 'https://', 'mailto:', 'tel:')):
                continue
            if tgt.startswith('#'):
                a = tgt[1:]
                if a not in SLUGMAP[os.path.normpath(f)]:
                    issues.append(f"Broken anchor: {f}:{ln} -> {tgt}")
                continue
            pp, a = (tgt.split('#', 1) + [None])[:2]
            tf = os.path.normpath(f) if pp == '' else os.path.normpath(os.path.join(d, pp))
            if not os.path.exists(tf):
                issues.append(f"Broken link: {f}:{ln} -> {tgt}")
                continue
            if a and tf in SLUGMAP and a not in SLUGMAP[tf]:
                issues.append(f"Broken anchor: {f}:{ln} -> {tgt}")

if issues:
    print(f"❌ {len(issues)} issue(s) found:\n")
    for i in issues:
        print("  -", i)
    sys.exit(1)

print(f"✅ {len(MD)} markdown files pass: no ASCII, balanced fences, "
      "valid Mermaid (fit-to-text labels), Sources present, 0 broken links/anchors.")
