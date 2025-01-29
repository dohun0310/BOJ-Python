n, m = map(int, input().split())
t = [[]] * n
l = []
r = 0
for i in range(n):
    t[i] = list(map(str, input().split()))
    s = 0
    for j in t[i]:
        if j.count("9") > 0:
            s += j.count("9")
            r += j.count("9")
    l.append(s)
for i in range(m):
    s = 0
    for j in range(n):
        if t[j][i].count("9") > 0:
            s += t[j][i].count("9")
    l.append(s)
print(r - max(l))