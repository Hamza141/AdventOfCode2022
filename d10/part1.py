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

X = 1
ans = 0
cycle = 0
cycles = [20, 60, 100, 140, 180, 220]
for l in lines:
    l = l.split()
    op = l[0]
    if op == 'addx':
        start = X
        for i in range(2):
            cycle += 1
            if cycle in cycles:
                ans += (cycle * start)
                print(cycle, start)
        X += int(l[1])
    else:
        cycle += 1
        if cycle in cycles:
            print(cycle, X)
            ans += (cycle * X)


print(ans)
