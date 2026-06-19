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
WIDTH = 40

SKIP = ('.git/', 'site/', 'site-src/', 'node_modules/')
MD = [p for p in glob.glob('**/*.md', recursive=True)
      if not any(s in (p + '/') for s in SKIP)]

NODE_LABEL = re.compile(r'([\[({]+)"([^"]*)"')


def wrap_text(s, width=WIDTH):
    out = []
    for part in s.split('<br/>'):
        line = ''
        for w in part.split(' '):
            if w == '':
                continue
            if line == '':
                line = w
            elif len(line) + 1 + len(w) <= width:
                line += ' ' + w
            else:
                out.append(line)
                line = w
        out.append(line)
    return '<br/>'.join(x for x in out if x != '')


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
