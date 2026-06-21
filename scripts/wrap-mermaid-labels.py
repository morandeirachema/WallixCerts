#!/usr/bin/env python3
"""Auto-wrap long Mermaid flowchart node labels so each box fits its text.

Mermaid sizes a node box to its widest line, so a long single-line label makes an
over-wide box. This rewraps NODE labels (quoted text after a node bracket [ ( {) in
`flowchart`/`graph` blocks to <= WIDTH chars per line by inserting <br/>, breaking only at
spaces (never inside a word). Existing <br/> breaks are kept; only over-long segments are
split. Edge labels ( |...| ) and non-flowchart diagrams are left untouched.

Run from anywhere:  python scripts/wrap-mermaid-labels.py
"""
import os
import re
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
WIDTH = 36  # max chars per node-label line (boxes are sized to the widest line)

SKIP = ('.git/', 'site/', 'site-src/', 'node_modules/')
MD = [p for p in glob.glob('**/*.md', recursive=True)
      if not any(s in (p + '/') for s in SKIP)]

NODE_LABEL = re.compile(r'([\[({]+)"([^"]*)"')


def _greedy(words, width):
    """Pack words into the fewest lines that each fit within `width`."""
    lines, line = [], ''
    for w in words:
        if line == '':
            line = w
        elif len(line) + 1 + len(w) <= width:
            line += ' ' + w
        else:
            lines.append(line)
            line = w
    if line:
        lines.append(line)
    return lines


def wrap_text(s, width=WIDTH):
    """Balanced wrap: use the fewest lines that fit in `width`, then make those
    lines as even as possible (avoids a long line next to a tiny orphan line).
    Existing <br/> breaks are honoured (each segment is wrapped independently)."""
    out = []
    for part in s.split('<br/>'):
        words = [w for w in part.split(' ') if w != '']
        if not words:
            continue
        target_lines = len(_greedy(words, width))
        # Shrink the effective width to the smallest that still fits in the same
        # number of lines, which balances line lengths and removes orphans.
        longest = max(len(w) for w in words)
        lo, hi, best = longest, width, width
        while lo <= hi:
            mid = (lo + hi) // 2
            if len(_greedy(words, mid)) <= target_lines:
                best, hi = mid, mid - 1
            else:
                lo = mid + 1
        out.extend(_greedy(words, best))
    return '<br/>'.join(out)


def rewrap_block(body):
    return NODE_LABEL.sub(lambda m: m.group(1) + '"' + wrap_text(m.group(2)) + '"', body)


def process(text):
    def block(m):
        body = m.group(1)
        first = next((l.strip() for l in body.splitlines() if l.strip()), '')
        if not first.startswith(('flowchart', 'graph')):
            return m.group(0)
        return '```mermaid\n' + rewrap_block(body) + '```'
    return re.sub(r'```mermaid\n(.*?)```', block, text, flags=re.S)


changed = 0
for f in MD:
    original = open(f, encoding='utf-8').read()
    new = process(original)
    if new != original:
        open(f, 'w', encoding='utf-8').write(new)
        changed += 1
        print("wrapped:", f)
print(f"\nDone — {changed} file(s) updated (wrap width {WIDTH}).")
