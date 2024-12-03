n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
x = [n // 2 - 1, n // 2]
y = [n // 2 - 1, n // 2]
s = 0
p = ""
t = [l[y[0] - 1][x[0]] + l[y[0] - 1][x[1]], l[y[1] + 1][x[0]] + l[y[1] + 1][x[1]], l[y[0]][x[0] - 1] + l[y[1]][x[0] - 1], l[y[0]][x[1] + 1] + l[y[1]][x[1] + 1]]
while True:
    m = max(t)
    if m <= 0:
        break
    s += m
    d = t.index(m)
    t[d] = 0
    if d == 0:
        p += "U"
        y[0] -= 1
        if y[0] > 0:
            for i in range(x[0], x[1] + 1):
                t[d] += l[y[0] - 1][i]
        if x[0] > 0:
            t[2] += l[y[0]][x[0] - 1]
        if x[1] < n - 1:
            t[3] += l[y[0]][x[1] + 1]
    elif d == 1:
        p += "D"
        y[1] += 1
        if y[1] < n - 1:
            for i in range(x[0], x[1] + 1):
                t[d] += l[y[1] + 1][i]
        if x[0] > 0:
            t[2] += l[y[1]][x[0] - 1]
        if x[1] < n - 1:
            t[3] += l[y[1]][x[1] + 1]
    elif d == 2:
        p += "L"
        x[0] -= 1
        if x[0] > 0:
            for i in range(y[0], y[1] + 1):
                t[d] += l[i][x[0] - 1]
        if y[0] > 0:
            t[0] += l[y[0] - 1][x[0]]
        if y[1] < n - 1:
            t[1] += l[y[1] + 1][x[0]]
    elif d == 3:
        p += "R"
        x[1] += 1
        if x[1] < n - 1:
            for i in range(y[0], y[1] + 1):
                t[d] += l[i][x[1] + 1]
        if y[0] > 0:
            t[0] += l[y[0] - 1][x[1]]
        if y[1] < n - 1:
            t[1] += l[y[1] + 1][x[1]]
print(s)
print(p)