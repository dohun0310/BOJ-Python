n = int(input())
l = [[0, 0]] + [[float("inf"), 0] for i in range(9999)]
a, b = 1, 2
while b <= n:
    for i in range(b, n + 1):
        l[i][0] = min(l[i][0], l[i - b][0] + a)
        l[i][1] = max(l[i][1], l[i - b][1] + a)
    b += a
    a = b - a
print(l[n][0], l[n][1])