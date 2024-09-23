n, s, m = map(int, input().split())
v = list(map(int, input().split()))
l = [[0] * (m + 1) for i in range(n + 1)]
l[0][s] = 1
for i in range(n):
    for j in range(m + 1):
        if l[i][j]:
            if j - v[i] >= 0:
                l[i + 1][j - v[i]] = 1
            if j + v[i] <= m:
                l[i + 1][j + v[i]] = 1
r = -1
for i in range(m + 1)[::-1]:
    if l[n][i]:
        r = i
        break
print(r)