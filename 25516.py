import sys
def dfs(s, e):
    global c
    v[s] = 1
    if e <= k:
        c += l[s]
    for i in g[s]:
        if not v[i]:
            dfs(i, e + 1)
sys.setrecursionlimit(10 ** 9)
n, k = map(int, sys.stdin.readline().split())
g = [[] for i in range(n)]
v = [0] * n
for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    g[a].append(b)
l = list(map(int, sys.stdin.readline().split()))
c = 0
dfs(0, 0)
print(c)