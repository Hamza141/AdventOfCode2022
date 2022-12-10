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
cycle = 0
cycles = [40, 80, 120, 160, 200, 240]

out = ''
ans = ''

for l in lines:
    l = l.split()
    if l[0] == 'addx':
        start = X
        for i in range(2):
            cycle += 1
            if X <= ((cycle - 1) % 40) + 1 <= X+2:
                out += '#'
            else:
                out += '.'

            if cycle in cycles:
                ans += out + '\n'
                out = ''
        X += int(l[1])

    else:
        cycle += 1

        if X <= ((cycle - 1) % 40) + 1 <= X+2:
            out += '#'
        else:
            out += '.'

        if cycle in cycles:
            ans += out + '\n'
            out = ''


print(ans)
