import re
from collections import deque

with open("aoc4.txt") as f:
    graph = [[*row] for row in f.read().strip().split()]

def partA(graph):
    R = len(graph)
    C = len(graph[0])

    horizontal = [''.join(r) for r in graph]
    vertical = []
    for c in range(C):
        tmp = []
        for r in range(R):
            tmp.append(graph[r][c])
        vertical.append(''.join(tmp))

    diag1 = []
    for r in range(R-1, -1, -1):
        row = r
        tmp = []
        for c in range(C-r):
            tmp.append(graph[row][c])
            row += 1
        diag1.append(''.join(tmp))

    for c in range(1, C):
        col = c
        tmp = []
        for r in range(R-c):
            tmp.append(graph[r][col])
            col += 1
        diag1.append(''.join(tmp))

    diag2 = []
    for r in range(R):
        row = r
        tmp = []
        for c in range(r+1):
            tmp.append(graph[row][c])
            row -= 1
        diag2.append(''.join(tmp))

    for c in range(1, C):
        col = c
        tmp = []
        for r in range(R-1, c-1, -1):
            tmp.append(graph[r][col])
            col += 1
        diag2.append(''.join(tmp))

    xmas1 = re.compile("(?=XMAS)")
    xmas2 = re.compile("(?=SAMX)")
    total = 0
    for substr in (horizontal + vertical + diag1 + diag2):
        total += len(xmas1.findall(substr))
        total += len(xmas2.findall(substr))
    return total


def partB(graph):
    R = len(graph)
    C = len(graph[0])
    directions = [(-1, -1), (1, 1), (1, -1), (-1, 1)]
    total = 0
    for r in range(1, R-1):
        for c in range(1, C-1):
            if graph[r][c] == 'A':
                mas = 0
                for d in directions:
                    new_r, new_c = r+d[0], c+d[1]
                    word = graph[new_r][new_c] + graph[r][c] + graph[r-d[0]][c-d[1]]
                    if word == 'MAS':
                        mas += 1
                    
                if mas == 2:
                    total += 1
    return total


print(partA(graph))
print(partB(graph))
