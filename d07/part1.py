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


class Directory():
    def __init__(self, curDir, par) -> None:
        self.children = {}
        self.curDir = curDir
        self.size = 0
        self.parent = par


root = Directory('/', None)
cur = root
for l in lines[1:]:
    if l[0] == '$':
        if 'cd' in l:
            if '..' in l:
                cur.parent.size += cur.size
                cur = cur.parent
            else:
                cur = cur.children[l.split(' ')[-1]]

        elif 'ls' in l:
            pass

    else:
        if 'dir' in l:
            cur.children[l.split(' ')[-1]] = Directory(l.split(' ')[-1], cur)
        else:
            cur.children[l.split(' ')[-1]] = int(l.split(' ')[0])
            cur.size += int(l.split(' ')[0])

dirs = []


def dfs(dir: Directory):
    if dir.size <= 100000:
        dirs.append(dir.size)
    for d in dir.children:
        if type(dir.children[d]) is Directory:
            dfs(dir.children[d])


dfs(root)

print(sum(dirs))
