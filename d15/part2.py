from tqdm import tqdm
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


mult = 4000000
biggest = 4000000

for x in tqdm(range(biggest+1)):
    invalid = []
    for i in range(len(sensors)):
        x1, y1 = sensors[i]
        x2, y2 = beacons[i]

        man_dist = abs(x1-x2) + abs(y1-y2)

        left = x1 - man_dist
        right = x1 + man_dist
        top = y1 - man_dist
        bottom = y1 + man_dist

        if left <= x <= right:
            diff = abs(x1 - x)
            # where x intersects the sensor diamond
            top = max(0, top + diff)
            bottom = min(biggest, bottom - diff)
            invalid.append((top, bottom))

    invalid.sort()
    totalStart, totalEnd = invalid[0]
    for start, end in invalid[1:]:
        if start <= totalEnd + 1:
            totalEnd = max(totalEnd, end)
        else:
            print(x)
            print((mult * x) + totalEnd + 1)
            exit(0)
