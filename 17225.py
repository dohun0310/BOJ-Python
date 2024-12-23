import sys
from collections import deque
s, j, n = map(int, sys.stdin.readline().split())
a = deque()
b = deque()
p, q = 0, 0
for i in range(n):
    t, c, m = sys.stdin.readline().rstrip().split()
    t = int(t)
    if c == "B":
        t = max(t, p)
        for i in range(int(m)):
            a.append([t, "B"])
            t += s
            p = t
    elif c == "R":
        t = max(t, q)
        for k in range(int(m)):
            b.append([t, "R"])
            t += j
            q = t
c = a + b
c = sorted(c, key=lambda x: [x[0], x[1]])
d, e = [], []
for k, v in enumerate(c):
    if v[1] == "B":
        d.append(k + 1)
    else:
        e.append(k + 1)
print(len(d))
print(*d)
print(len(e))
print(*e)