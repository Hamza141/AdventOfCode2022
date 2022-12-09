import math
import re
import heapq
from collections import defaultdict, deque
from os.path import dirname, abspath, join
import numpy as np


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile(join(dirname(abspath(__file__)), 'input.txt'))

res = 0

ROWS = 1000
COLS = 1000
graph = [[0] * COLS for _ in range(ROWS)]
start = (ROWS//2, COLS//2)
head = start
tail = start

dirs = {'R': (0, 1), 'U': (-1, 0),
        'L': (0, -1), 'D': (1, 0)}

for l in lines:
    dir = l[0]
    dist = int(l[2:])
    d = dirs[dir]

    while dist > 0:
        head = (head[0] + d[0], head[1] + d[1])
        tr = tail[0]
        tc = tail[1]
        hr = head[0]
        hc = head[1]

        if abs(tr - hr) > 1 or abs(tc - hc) > 1:
            if head[0] == tail[0] or head[1] == tail[1]:
                tr += d[0]
                tc += d[1]
            else:
                if dir == 'U':
                    tr -= 1
                    tc = hc
                elif dir == 'L':
                    tr = hr
                    tc -= 1
                elif dir == 'D':
                    tr += 1
                    tc = hc
                elif dir == 'R':
                    tr = hr
                    tc += 1
        else:
            tail = (tr, tc)
            a = 1
        tail = (tr, tc)

        if abs(tr - hr) > 1 or abs(tc - hc) > 1:
            a = 2
        dist -= 1
        if graph[tail[0]][tail[1]] == 0:
            res += 1
        graph[tail[0]][tail[1]] = 1

print(res)
