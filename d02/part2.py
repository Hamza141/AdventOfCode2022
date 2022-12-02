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
loses = {'Z': 'X', 'X': 'Y', 'Y': 'Z'}
score = {'X': 1, 'Y': 2, 'Z': 3}
res = 0

for l in lines:
    opp = d[l[0]]
    round = l[-1]

    if round == 'Y':
        res += 3
        res += score[opp]
    elif round == 'Z':
        res += 6
        res += score[loses[opp]]
    else:
        res += score[beats[opp]]

print(res)
