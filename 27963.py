a, b, x = map(int, input().split())
n, m = min(a, b), max(a, b)
v = (100 - x) / n
v += x / m
print(100 / v)