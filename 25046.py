from itertools import combinations
n = int(input())
l = [[]] * n
for i in range(n):
    l[i] = list(map(int, input().split()))
m = list(range(0, n))
c = list()
for i in range(n + 1):
    for j in combinations(m, i):
        c.append(j)
a = -(float("inf"))
s = list()
for i in range(n):
    t = 0
    for j in range(n):
        t += l[j][i]
    s.append(t)
for i in c:
    h = 0
    for j in range(n):
        t= 0
        for k in i:
            t += l[k][j]
        h += min(s[j] - t , t)
    a = max(h, a)
print(a)