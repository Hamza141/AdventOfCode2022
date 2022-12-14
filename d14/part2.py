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

res = 0
ROWS = 0
START = END = 500

points = []
for i, l in enumerate(lines):
    l = l.split('->')
    row = []
    for p in l:
        x, y = p.split(',')
        x = int(x.strip())
        y = int(y.strip())
        START = min(START, x)
        END = max(END, x + 1)
        ROWS = max(ROWS, y + 1)
        row.append((x, y))
    points.append(row)

END += 250
START -= 150
ROWS += 2

COLS = END - START

graph = [['.'] * COLS for _ in range(ROWS)]


for i in range(COLS):
    graph[-1][i] = '#'


def getX(x):
    return x - START


for row in points:
    i = 0
    while i < len(row) - 1:
        if row[i][0] == row[i+1][0]:
            # vertical
            _start = min(row[i][1], row[i+1][1])
            _end = max(row[i][1], row[i+1][1])
            X = getX(row[i][0])
            while _start <= _end:
                graph[_start][X] = '#'
                _start += 1
        else:
            # horizontal
            _start = min(row[i][0], row[i+1][0])
            _end = max(row[i][0], row[i+1][0])
            Y = row[i][1]
            while _start <= _end:
                X = getX(_start)
                graph[Y][X] = '#'
                _start += 1
        i += 1


def checkDown(x, y):
    if y + 1 < ROWS and x < COLS and graph[y+1][x] == '.':
        return True
    return False


def checkLeft(x, y):
    if y + 1 < ROWS and x - 1 < COLS and graph[y+1][x-1] == '.':
        return True
    return False


def checkRight(x, y):
    if y + 1 < ROWS and x + 1 < COLS and graph[y+1][x+1] == '.':
        return True
    return False


sand = (500, 0)
while True:
    x = getX(sand[0])
    y = sand[1]

    oldRes = res
    while True:
        while checkDown(x, y):
            y += 1

        if checkLeft(x, y):
            x -= 1
            y += 1
        elif checkRight(x, y):
            x += 1
            y += 1
        else:
            if x <= 0 or x >= COLS or y >= ROWS - 1:
                break

            if graph[y][x] == '.':
                graph[y][x] = 'O'
                res += 1
            break

    if oldRes == res:
        break

print(res)
