import sys
def row(x, n):
    for i in range(9):
        if n == l[x][i]:
            return False
    return True
def col(y, n):
    for i in range(9):
        if n == l[i][y]:
            return False
    return True
def squ(x, y, n):
    for i in range(3):
        for j in range(3):
            if n == l[x // 3 * 3 + i][y // 3 * 3 + j]:
                return False
    return True
def back(n):
    if n == len(t):
        for i in l:
            print(*i)
        exit()
    for i in range(1, 10):
        x, y = t[n]
        if row(x, i) and col(y, i) and squ(x, y, i):
            l[x][y] = i
            back(n + 1)
            l[x][y] = 0
l = [list(map(int, sys.stdin.readline().split())) for i in range(9)]
t = []
for i in range(9):
    for j in range(9):
        if l[i][j] == 0:
            t.append((i, j))
back(0)