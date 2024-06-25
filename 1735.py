from math import gcd
a, b = map(int, input().split())
c, d = map(int, input().split())
o, p = a * d + c * b, b * d
n = gcd(o, p)
print(o // n, p // n)