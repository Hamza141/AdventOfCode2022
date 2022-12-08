import math
import re
import heapq
from collections import defaultdict, deque
from os.path import dirname, abspath, join


def readFile(filename):
    lines = []
    with open(filename, 'r') as f:
        for line in f:
            lines.append(line.strip())
    return lines


lines = readFile(join(dirname(abspath(__file__)), 'input.txt'))

res = 0

adjList = []

for l in lines:
    row = []
    for c in l:
        row.append(int(c))
    adjList.append(row)

ROWS = len(adjList)
COLS = len(adjList[0])

def dfs(i, j, start, d):
    if i < 0 or i == ROWS or j < 0 or j == COLS:
        return 0

    if adjList[i][j] >= start:
        return 1

    return dfs(i+d[0], j+d[1], start, d) + 1

dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]
for i in range(1, ROWS - 1):
    for j in range(1, COLS - 1):
        cur = adjList[i][j]
        score = 1
        for d in dirs:
            score *= dfs(i+d[0], j+d[1], cur, d)
        res = max(score, res)
print(res)
