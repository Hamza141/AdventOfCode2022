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

res = 0

for l in lines:
    mid = int(len(l)/2)
    first = set(l[:mid])
    second = set(l[-mid:])
    inter = first.intersection(second)
    found = inter.pop()
    if 'A' <= found <= 'Z':
        res += ord(found) - ord('A') + 27
    else:
        res += ord(found) - ord('a') + 1

print(res)
