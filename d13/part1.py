import json
import math
import re
import heapq
from collections import defaultdict, deque
from os.path import dirname, abspath, join
import numpy as np
import copy


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile(join(dirname(abspath(__file__)), 'input.txt'))


def compare(left, right):
    li = ri = out = 0
    while True:
        if li == len(left) and ri == len(right):
            return 0
        elif ri == len(right):
            return 1
        elif li == len(left):
            return -1

        if type(left[li]) is int and type(right[ri]) is int:
            if left[li] < right[ri]:
                return -1
            elif left[li] > right[ri]:
                return 1
        elif type(left[li]) is list and type(right[ri]) is list:
            out = compare(left[li], right[ri])
        elif type(left[li]) is list:
            out = compare(left[li], [right[ri]])
        elif type(right[ri]) is list:
            out = compare([left[li]], right[ri])
        if out in [-1, 1]:
            return out

        li += 1
        ri += 1


res = 0
for i in range(0, len(lines), 3):
    if compare(json.loads(lines[i]), json.loads(lines[i+1])) == -1:
        res += (i // 3) + 1
print(res)
