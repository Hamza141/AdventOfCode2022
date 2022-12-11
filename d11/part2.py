import math
import re
import heapq
from collections import defaultdict, deque
from os.path import dirname, abspath, join
import numpy as np


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


class Monkey():
    def __init__(self, id) -> None:
        self.id = id
        self.items = []
        self.op = None
        self.test = None
        self.trueThrow = -1
        self.falseThrow = -1
        self.inspections = 0


magic_num = 1
monkeys = []
for l in lines:
    if l.startswith('Monkey'):
        l = l.split()
        monkeys.append(Monkey(int(l[1][:-1])))
    elif 'items' in l:
        l = l.split(':')[1].split(',')
        for item in l:
            monkeys[-1].items.append(int(item.strip()))
    elif 'Operation' in l:
        l = l.split('=')[1]
        monkeys[-1].op = l
    elif 'Test' in l:
        l = l.split('by')
        monkeys[-1].test = int(l[1].strip())
        magic_num *= int(l[1].strip())
    elif 'true' in l:
        monkeys[-1].trueThrow = int(l[-1])
    elif 'false' in l:
        monkeys[-1].falseThrow = int(l[-1])

for i in range(10000):
    for m in monkeys:
        for old in m.items:
            new = eval(m.op)
            new = new % magic_num
            if new % m.test == 0:
                monkeys[m.trueThrow].items.append(new)
            else:
                monkeys[m.falseThrow].items.append(new)
            m.inspections += 1
        m.items = []

inspections = sorted([m.inspections for m in monkeys])
print(inspections[-1] * inspections[-2])
