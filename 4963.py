import sys
from collections import deque
def bfs(v, e, f, x, y):
    v[y][x] = 0
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + e[i]
            ny = y + f[i]
            if 0 <= nx < w and 0 <= ny < h and v[ny][nx] == 1:
                q.append((nx, ny))
                v[ny][nx] = 0
e = [-1, 1, 0, 0, -1, 1, 1, -1]
f = [0, 0, -1, 1, 1, -1, 1, -1]
while True:
    w, h = map(int, sys.stdin.readline().split())
    if not w and not h:
        break
    c = 0
    g = [[0] * w for i in range(h)]
    for i in range(h):
        g[i] = list(map(int, sys.stdin.readline().split()))
    for y in range(h):
        for x in range(w):
            if g[y][x]:
                bfs(g, e, f, x, y)
                c += 1
    print(c)