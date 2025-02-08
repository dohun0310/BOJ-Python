n = int(input())
v = [0, 0] + [1] * (n - 1)
l = []
for i in range(2, n + 1):
    if v[i]:
        l.append(i)
        for j in range(i * i, n + 1, i):
            v[j] = 0
s, e, a = 0, 0, 0
while e <= len(l):
    if sum(l[s:e]) >= n:
        if sum(l[s:e]) == n:
            a += 1
        s += 1
    else:
        e += 1
print(a)