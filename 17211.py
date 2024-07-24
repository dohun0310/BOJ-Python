n, f = map(int, input().split())
h, j, k, l = map(float, input().split())
g, b = 0.0, 0.0
if f:
    b = 1.0
else:
    g = 1.0
for i in range(n):
    t = g
    g, b = g * h + b * k, t * j + b * l
print(int(g * 1000))
print(int(b * 1000))