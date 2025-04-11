import sys
r, c = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
d = {}
for i in range(n):
    a, v, h = map(int, sys.stdin.readline().split())
    if a not in d:
        d[a] = [v, v, h, h]
    else:
        d[a][0] = min(d[a][0], v)
        d[a][1] = max(d[a][1], v)
        d[a][2] = min(d[a][2], h)
        d[a][3] = max(d[a][3], h)
b = None
m = -1
for i in d:
    e = (d[i][1] - d[i][0] + 1) * (d[i][3] - d[i][2] + 1)
    if e > m or (e == m and (b is None or i < b)):
        m = e
        b = i
print(b, m)