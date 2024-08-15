import sys
import math
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
e = math.lcm(a[0], b[0])
n, m = e, e
i = a[1] * (e // a[0]) + b[1] * (e // b[0])
j = a[1] * (e // a[0]) - b[1] * (e // b[0])
k = a[2] * (e // a[0]) + b[2] * (e // b[0])
l = a[2] * (e // a[0]) - b[2] * (e // b[0])
t = math.gcd(math.gcd(n, i), math.gcd(n, k))
if t > 1:
    n //= t
    i //= t
    k //= t
t = math.gcd(math.gcd(m, j), math.gcd(m, l))
if t > 1:
    m //= t
    j //= t
    l //= t
if k == 0:
    print(n, i, k, 0)
else:
    print(n, i, k, a[3])
if l == 0:
    print(m, j, l, 0)
else:
    print(m, j, l, a[3])
o, p = a[1] * b[1] + a[2] * b[2] * a[3], a[1] * b[2] + b[1] * a[2]
if p == 0:
    t = math.gcd(a[0] * b[0], o)
    print(a[0] * b[0] // t, o // t, 0, 0)
else:
    t = math.gcd(math.gcd(a[0] * b[0], o), math.gcd(a[0] * b[0], p))
    print(a[0] * b[0] // t, o // t, p // t, a[3])
s = a[0] * (b[1] ** 2 - a[3] * (b[2] ** 2))
o, p = b[0] * (a[1] * b[1] + a[2] * (-b[2]) * a[3]), b[0] * (a[1] * (-b[2]) + b[1] * a[2])
if p == 0:
    t = math.gcd(s, o)
    if s / t < 0:
        print(-(s // t), -(o // t), 0, 0)
    else:
        print(s // t, o // t, 0, 0)
else:
    t = math.gcd(math.gcd(s, o), math.gcd(s, p))
    if s / t < 0:
        print(-(s // t), -(o // t), -(p // t), a[3])
    else:
        print(s // t, o // t, p // t, a[3])