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

sensors = []
beacons = []
for i, l in enumerate(lines):
    l = l.split()
    x1 = int(l[2].split('=')[1][:-1])
    y1 = int(l[3].split('=')[1][:-1])
    sensors.append((x1, y1))

    x2 = int(l[-2].split('=')[1][:-1])
    y2 = int(l[-1].split('=')[1])
    beacons.append((x2, y2))


n = set()
ry = 2000000

for i in range(len(sensors)):
    x1, y1 = sensors[i]
    x2, y2 = beacons[i]

    man_dist = abs(x1-x2) + abs(y1-y2)

    left = x1 - man_dist
    right = x1 + man_dist
    const = abs(ry-y1)

    for x in range(min(left, right)-1, max(left, right)+1):
        if (abs(x-x1) + const) <= man_dist:
            n.add((x, ry))
    n.discard((x1, y1))
    n.discard((x2, y2))
print(len(n))
