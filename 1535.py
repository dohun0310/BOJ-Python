n = int(input())
t = [0] + list(map(int, input().split()))
p = [0] + list(map(int, input().split()))
l = [[0] * 101 for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, 101):
        if t[i] <= j:
            l[i][j] = max(l[i - 1][j], l[i - 1][j - t[i]] + p[i])
        else:
            l[i][j] = l[i - 1][j]
print(l[n][99])