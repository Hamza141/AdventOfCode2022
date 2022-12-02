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
ans = []
for l in lines:
    if not l:
        ans.append(cur)
        cur = 0
    else:
        cal = int(l)
        cur += cal
if l:
    ans.append(cur)
print(sum(sorted(ans)[-3:]))