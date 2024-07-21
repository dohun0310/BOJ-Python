n = int(input())
m = int(input())
l = [[0] * (m + 1) for i in range(n + 1)]
l[0][0] = 1
for i in range(1, n + 1):
    for j in range(i, m + 1):
        l[i][j] = l[i][j - 1] + l[i - 1][j - 1]
print(l[n][m])