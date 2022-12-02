import math
import re
import heapq
import sys
from collections import defaultdict
from os.path import dirname, abspath, join


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile(join(dirname(abspath(__file__)), 'input.txt'))

d = {'A': 'X', 'B': 'Y', 'C': 'Z'}
beats = {'X': 'Z', 'Y': 'X', 'Z': 'Y'}
score = {'X': 1, 'Y': 2, 'Z': 3}
res = 0

for l in lines:
    opp = d[l[0]]
    you = l[-1]

    res += score[you]

    if you == opp:
        res += 3
    elif you != beats[opp]:
        res += 6

print(res)
