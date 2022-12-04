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
    l = l.split(',')
    left = l[0].split('-')
    right = l[1].split('-')
    if int(left[0]) >= int(right[0]) and int(left[1]) <= int(right[1]):
        res += 1
    elif int(right[0]) >= int(left[0]) and int(right[1]) <= int(left[1]):
        res += 1

print(res)
