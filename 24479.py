import sys
sys.setrecursionlimit(10 ** 6)
def dfs(v, e, r):
    global c
    v[r] = c
    for x in e[r]:
        if not v[x]:
            c += 1
            dfs(v, e, x)
n, m, r = map(int, sys.stdin.readline().split())
c = 1
g = [[] for i in range(n + 1)]
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    g[u].append(v)
    g[v].append(u)
for i in range(n + 1):
    g[i].sort()
v = [0] * (n + 1)
dfs(v, g, r)
for i in range(1, n + 1):
    print(v[i])