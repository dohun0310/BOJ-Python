n, l, k = map(int, input().split())
s = [list(map(int, input().split())) for i in range(n)]
a, b = 0, 0
for i, j in s:
    if i <= l and j <= l:
        a += 1
    elif i <= l:
        b += 1
if a + b < k:
    print(140 * a + 100 * b)
else:
    if a > k:
        a = k
    t = k - a
    print(140 * a + 100 * t)