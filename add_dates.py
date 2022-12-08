#!/usr/bin/env python3

import os.path as path
import datetime
ts = datetime.date(2022, 12, 4)
week = datetime.timedelta(days=7)

mnames = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December']

entries = []
with open('index.md') as inf:
    for l in inf.read().split('\n'):
        if l.startswith('* ['):
            entries.append(l[l.index('(') + 1:l.index(')')])

for e in reversed(entries):
    with open(e) as inf:
        lines = inf.read().split('\n')
    with open(e, 'w') as ouf:
        while lines and not lines[0].startswith('#'):
            ouf.write(lines.pop(0) + '\n')
        ouf.write(lines.pop(0) + '\n')
        ouf.write("%d %s, %d\n\n" % (ts.day, mnames[ts.month - 1], ts.year))
        ts = ts - week
        ouf.write('\n'.join(lines))
