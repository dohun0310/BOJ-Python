import math
n, m = map(int, input().split())
x, y = map(int, input().split())
p = 0
c = 0
for i in range(m):
    a, b = map(int, input().split())
    if a != 0:
        p += 1
    else:
        c += 1
n -= p
s = 1
if c > 0:
    s *= math.comb(n, c) * math.factorial(c)
n -= c
if n > 0:
    s *= math.perm(9 - (p + c), n)
print(s * x + ((s - 1) // 3) * y)