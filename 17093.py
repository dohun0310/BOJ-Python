n, m = map(int, input().split())
x = [0] * n
y = [0] * n
a = [0] * m
b = [0] * m
for i in range(n):
    x[i], y[i] = map(int, input().split())
for i in range(m):
    a[i], b[i] = map(int, input().split())
s = 0
for i in range(n):
    for j in range(m):
        t = (x[i] - a[j]) ** 2 + (y[i] - b[j]) ** 2
        if t > s:
            s = t
print(s)