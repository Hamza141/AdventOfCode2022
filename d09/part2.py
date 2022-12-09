import math
import re
import heapq
from collections import defaultdict, deque
from os.path import dirname, abspath, join
import numpy as np


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

seen = set()

ROWS = 1000
COLS = 1000
graph = [['.'] * COLS for _ in range(ROWS)]
start = (ROWS//2, COLS//2)
chain = [start] * 10

dirs = {'R': (0, 1), 'U': (-1, 0),
        'L': (0, -1), 'D': (1, 0)}

for l in lines:
    dir = l[0]
    dist = int(l[2:])
    d = dirs[dir]
    while dist > 0:
        graph[chain[0][0]][chain[0][1]] = '.'
        chain[0] = (chain[0][0] + d[0], chain[0][1] + d[1])
        graph[chain[0][0]][chain[0][1]] = 'H'
        for i in range(1, len(chain)):
            tr = chain[i][0]
            tc = chain[i][1]
            hr = chain[i-1][0]
            hc = chain[i-1][1]
            if i != len(chain) - 1:
                graph[chain[i][0]][chain[i][1]] = '.'
            
            if abs(tr - hr) > 1 or abs(tc - hc) > 1:
                if hr - tr > 0:
                    tr += 1
                elif tr - hr > 0:
                    tr -= 1
                
                if hc - tc > 0:
                    tc += 1
                elif tc - hc > 0:
                    tc -= 1

            chain[i] = (tr, tc)
            graph[chain[i][0]][chain[i][1]] = i

        graph[chain[-1][0]][chain[-1][1]] = '#'
        seen.add(chain[-1])
        dist -= 1

print(len(seen))
