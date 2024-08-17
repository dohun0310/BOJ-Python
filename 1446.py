import sys
n, d = map(int, sys.stdin.readline().split())
l = [i for i in range(d + 1)]
g = []
for i in range(n):
    s, a, b = map(int, sys.stdin.readline().split())
    if a - s > b:
        g.append([s, a, b])
g.sort()
for i, j, k in g:
    for x in range(1, d + 1):
        if j == x:
            l[x] = min(l[x], l[i] + k)
        else:
            l[x] = min(l[x], l[x - 1] + 1)
print(l[d])