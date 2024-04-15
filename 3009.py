x = []
y = []
a = 0
b = 0
for i in range(3):
    n, m = map(int, input().split())
    x.append(n)
    y.append(m)
for i in range(3):
    if x.count(x[i]) == 1:
        a = x[i]
    if y.count(y[i]) == 1:
        b = y[i]
print(a, b)