import sys
n, m = map(int, sys.stdin.readline().split())
l = []
t = 0
for i in range(n):
    c = int(sys.stdin.readline())
    l.append(t + c - 1)
    t += c
l.append(int(1e12))
for i in range(m):
    s, e, j = 0, len(l), int(sys.stdin.readline())
    while s < e:
        m = (s + e) // 2
        if l[m] < j:
            s = m + 1
        else:
            e = m
    print(e + 1)