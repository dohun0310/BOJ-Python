def back(a, t):
    global s
    if a == m:
        r = 0
        for i in h:
            d = 1e9
            for j in range(len(c)):
                if v[j]:
                    d = min(d, abs(i[0] - c[j][0]) + abs(i[1] - c[j][1]))
            r += d
        s = min(s, r)
        return
    else:
        for i in range(t, len(c)):
            if not v[i]:
                v[i] = 1
                back(a + 1, i + 1)
                v[i] = 0
n, m = map(int, input().split())
h, c = [], []
for i in range(n):
    l = list(map(int, input().split()))
    for j in range(n):
        if l[j] == 1:
            h.append((i, j))
        elif l[j] == 2:
            c.append((i, j))
v = [0] * len(c)
s = 1e9
back(0, 0)
print(s)