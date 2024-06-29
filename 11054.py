n = int(input())
a = list(map(int, input().split()))
o, p = [1] * n, [1] * n
s = 0
for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            o[i] = max(o[i], o[j] + 1)
        if a[::-1][i] > a[::-1][j]:
            p[i] = max(p[i], p[j] + 1)
for i in range(n):
    s = max(s, o[i] + p[::-1][i])
print(s - 1)