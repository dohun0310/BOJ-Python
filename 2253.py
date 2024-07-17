n, m = map(int, input().split())
s = set()
for i in range(m):
    s.add(int(input()))
l = [[10001] * (int((n * 2) ** 0.5) + 2) for i in range(n + 1)]
l[1][0] = 0
for i in range(2, n + 1):
    if i in s:
        continue
    for j in range(1, int((i * 2) ** 0.5) + 1):
        l[i][j] = min(l[i - j][j - 1], l[i - j][j], l[i - j][j + 1]) + 1
if min(l[n]) == 10001:
    print(-1)
else:
    print(min(l[n]))