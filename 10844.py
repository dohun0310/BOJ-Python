n = int(input())
l = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1]] + [[0] * 10 for i in range(n - 1)]
for i in range(1, n):
    l[i][0] = l[i - 1][1]
    l[i][9] = l[i - 1][8]
    for j in range(1, 9):
        l[i][j] = l[i - 1][j - 1] + l[i - 1][j + 1]
print(sum(l[n - 1]) % 1000000000)