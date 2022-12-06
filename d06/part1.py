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
            lines.append(line.strip())
    return lines


lines = readFile(join(dirname(abspath(__file__)), 'input.txt'))

d = deque()
res = 1

for l in lines:
    for c in l:
        while c in d:
            d.popleft()
        d.append(c)
        if len(d) == 4:
            break
        res += 1

print(res)
