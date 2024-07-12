import sys
sys.setrecursionlimit(10000)
n, m = map(int, sys.stdin.readline().split())
g = [[] for i in range(n + 1)]
for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    g[u].append(v)
    g[v].append(u)
c = 0
l = [False] * (n + 1)
def dfs(x):
    if l[x]: return
    l[x] = True
    for i in g[x]: dfs(i)
for i in range(1, n + 1):
    if not l[i]:
        dfs(i)
        c += 1
print(c)