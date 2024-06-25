import sys
n, m = map(int, sys.stdin.readline().split())
l = {}
for i in range(n):
    t = sys.stdin.readline().rstrip()
    if len(t) < m:
        continue
    else:
        if t in l:
            l[t] += 1
        else:
            l[t] = 1
s = sorted(l.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in s:
    print(i[0])