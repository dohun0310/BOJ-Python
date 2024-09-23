n, m = map(int, input().split())
d = {}
for i in range(n):
    q, a = input().split()
    d[q] = a
for i in range(m):
    s = input()
    t = ""
    for j in range(len(s)):
        for k in sorted(d.keys()):
            if s.find(k, j) == j:
                t += d[k]
    if t:
        print(t)
    else:
        print(-1)