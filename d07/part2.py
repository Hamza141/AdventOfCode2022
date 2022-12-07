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


class Directory():
    def __init__(self, curDir, par) -> None:
        self.children = {}
        self.curDir = curDir
        self.size = 0
        self.parent = par
        # self.seen = False


root = Directory('/', None)
cur = root
for l in lines[1:]:
    if l[0] == '$':
        if 'cd' in l:
            if '..' in l:
                cur.parent.size += cur.size
                cur = cur.parent
            else:
                # if not cur.children[l.split(' ')[-1]].seen:
                cur = cur.children[l.split(' ')[-1]]

        elif 'ls' in l:
            pass

    else:
        if 'dir' in l:
            cur.children[l.split(' ')[-1]] = Directory(l.split(' ')[-1], cur)
        else:
            cur.children[l.split(' ')[-1]] = int(l.split(' ')[0])
            cur.size += int(l.split(' ')[0])

while cur != root:
    cur.parent.size += cur.size
    cur = cur.parent

space_available = 70000000 - root.size
space_needed = 30000000 - space_available

dirs = []


def dfs(dir: Directory):
    if dir.size >= space_needed:
        dirs.append(dir.size)
    for d in dir.children:
        if type(dir.children[d]) is Directory:
            dfs(dir.children[d])


dfs(root)

print(sorted(dirs)[0])
