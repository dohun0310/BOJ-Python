a = input()
b = input()
x = "0" + a
y = "0" + b
l = [[0] * (len(a) + 1) for _ in range(len(y) + 1)]
for i in range(1, len(y)):
    for j in range(1, len(x)):
        if x[j] == y[i]:
            l[i][j] = l[i - 1][j - 1] + 1
        else:
            l[i][j] = max(l[i - 1][j], l[i][j - 1])
t = 0
for i in l:
    if t < max(i):
        t = max(i)
print(len(a) + len(b) - t)