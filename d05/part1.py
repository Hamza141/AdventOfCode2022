import math
import re
import heapq
import sys
from collections import defaultdict, deque
from os.path import dirname, abspath, join


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line)
    return lines


lines = readFile(join(dirname(abspath(__file__)), 'input.txt'))

d = defaultdict(deque)

for l in lines:
    if '[' in l:
        col = 0
        cur = 1 + (4 * col)
        while cur <= len(l):
            if l[cur] != ' ':
                d[col+1].appendleft(l[cur])
            col += 1
            cur = 1 + (4 * col)

    elif 'move' in l:
        l = l.split()
        count = int(l[1])
        frm = int(l[-3])
        to = int(l[-1])
        while count > 0 and d[frm]:
            d[to].append(d[frm].pop())
            count -= 1

ans = ''
cur = 1
while cur in d:
    if d[cur]:
        ans += d[cur][-1]
    cur += 1
print(ans)
