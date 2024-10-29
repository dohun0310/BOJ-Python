n = int(input())
l = [[0, 0, 0]] * n
for i in range(n):
    l[i] = list(map(int, input().split()))
l.sort()
d = [0] * n
d[0] = l[0][2]
for i in range(1, n):
    d[i] = max(d[i - 1], d[i - 2] + l[i][2])
print(d[n - 1])