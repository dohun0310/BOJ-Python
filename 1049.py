n, m = map(int, input().split())
y = [0] * m
h = [0] * m
for i in range(m):
    y[i], h[i] = map(int, input().split())
y, h = min(y), min(h)
if y < h * 6:
    if y < (n % 6) * h:
        print((n // 6) * y + y)
    else:
        print((n // 6) * y + (n % 6) * h)
else:
    print(n * h)