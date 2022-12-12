import math
import re
import heapq
from collections import defaultdict, deque
from os.path import dirname, abspath, join
import numpy as np
import copy


def print_graph(graph):
    print()
    for row in graph:
        print(*row, sep='')


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile(join(dirname(abspath(__file__)), 'input.txt'))

res = 0
ROWS = len(lines)
COLS = len(lines[0])
graph = [[''] * COLS for _ in range(ROWS)]

starts = []
for i, l in enumerate(lines):
    for j, c in enumerate(l):
        if c == 'S':
            c = 'a'
        if c == 'a':
            starts.append((i, j))
        graph[i][j] = c

q = deque()
seen = set()

for start in starts:
    q.append((start[0], start[1], 'a', 0))

dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
while q:
    i, j, prev, steps = q.popleft()

    if i < 0 or i >= ROWS or j < 0 or j >= COLS or (i, j) in seen:
        continue

    cur = graph[i][j]

    if cur == 'E':
        if prev == 'z':
            print(steps)
            break
        continue

    if ord(cur) > ord(prev) + 1:
        continue

    seen.add((i, j))
    for d in dirs:
        if (i+d[0], j+d[1]) not in seen:
            q.append((i+d[0], j+d[1], cur, steps+1))
