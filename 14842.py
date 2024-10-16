w, h, n = map(int, input().split())
s = 0
for i in range(1, n):
    x = min(w / n * i, w - w / n * i)
    y = h * x / (w / 2)
    s += h - y
print(f"{s:.6f}")