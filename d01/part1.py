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

cur = 0
ans = 0
for l in lines:
    if not l:
        if cur > ans:
            ans = cur
        cur = 0
    else:
        cal = int(l)
        cur += cal
print(max(ans, cur))