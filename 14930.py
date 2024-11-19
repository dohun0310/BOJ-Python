import sys
n, t = map(int, sys.stdin.readline().split())
v = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
r = v[0]
v.sort()
i = v.index(r)
p = [x + y * t for x, y in v]
p.sort()
print(p[i])