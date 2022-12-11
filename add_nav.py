#!/usr/bin/env python3

import os.path as path

entries = []
with open('index.md') as inf:
    for l in inf.read().split('\n'):
        if l.startswith('* ['):
            entries.append(l[l.index('(') + 1:l.index(')')])

for i in range(len(entries)):
    with open(entries[i]) as inf:
        lines = inf.read().split('\n')
    while lines and not lines[0].startswith('#'):
        lines.pop(0)
    assert lines
    prev = entries[i - 1] if i > 0 else None
    if prev: prev = path.relpath(prev, path.dirname(entries[i]))
    next = entries[i + 1] if i < len(entries) - 1 else None
    if next: next = path.relpath(next, path.dirname(entries[i]))
    with open(entries[i], 'w') as ouf:
        ouf.write('<span><p align=center>\n')
        if prev: ouf.write('[prev](%s)&emsp;\n' % prev)
        ouf.write('[top](../index.md)&emsp;\n')
        if next: ouf.write('[next](%s)\n' % next)
        ouf.write('</p></span>\n')
        ouf.write('\n'.join(lines))
