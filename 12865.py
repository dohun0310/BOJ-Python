n, k = map(int, input().split())
l = [[0, 0] for _ in range(n + 1)]
s = [[0] * (k + 1) for _ in range(n + 1)]
for i in range(n):
    l[i + 1] = list(map(int, input().split()))
for i in range(1, n + 1):
    for j in range(1, k + 1):
        if j < l[i][0]:
            s[i][j] = s[i - 1][j]
        else:
            s[i][j] = max(s[i - 1][j], s[i - 1][j - l[i][0]] + l[i][1])
print(s[n][k])