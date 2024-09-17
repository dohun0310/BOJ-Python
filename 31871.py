import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
g = [[] for i in range(n+1)]
for i in range(m):
    u, v, d = map(int, sys.stdin.readline().split())
    g[u].append((v, d))
l = [[-1] * (1 << n) for i in range(n + 1)]
for i in g[0]:
    v, d = i
    if v == 0:
        continue
    s = 1 << (v - 1)
    if l[v][s] < d:
        l[v][s] = d
for i in range(1 << n):
    for j in range(1, n + 1):
        if l[j][i] == -1:
            continue
        for k in g[j]:
            v, d = k
            if v == 0:
                continue
            if (i >> (v - 1)) & 1:
                continue
            t = i | (1 << (v - 1))
            if l[v][t] < l[j][i] + d:
                l[v][t] = l[j][i] + d
s = -1
t = (1 << n) -1
for i in range(1, n + 1):
    if l[i][t] == -1:
        continue
    for j in g[i]:
        v, d = j
        if v != 0:
            continue
        if s < l[i][t] + d:
            s = l[i][t] + d
print(s if s != -1 else -1)