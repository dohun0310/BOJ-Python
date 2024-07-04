def multi(a, b):
    l = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                l[i][j] += a[i][k] * b[k][j] % 1000
    return l
def square(a, b):
    if b == 1:
        return a
    t = square(a, b // 2)
    if b % 2:
        return multi(multi(t, t), a)
    return multi(t, t)
n, b = map(int, input().split())
a = [[*map(int, input().split())] for i in range(n)]
s = square(a, b)
for i in range(n):
    for j in range(n):
        s[i][j] %= 1000
for i in s:
    print(*i)