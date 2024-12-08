n, a, b = map(int, input().split())
x = sorted(list(map(int, input().split())))
y = sorted(list(map(int, input().split())))
s = 0
if n % 2 == 1:
    s += x[-1]
    x.pop(-1)
    n -= 1
for i in range(0, n, 2):
    n, m = 0, 0
    if len(x) >= 2:
        n = x[-1] + x[-2]
    if len(y) >= 1:
        m = y[-1]
    if n > m:
        s += n
        x.pop()
        x.pop()
    else:
        s += m
        y.pop()
print(s)