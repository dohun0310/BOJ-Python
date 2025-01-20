import math
n = int(input())
a = int(input())
l = [0] * (n - 1)
for i in range(n - 1):
    t = int(input())
    l[i] = t - a
    a = t
g = l[0]
for i in range(1, n - 1):
    g = math.gcd(g, l[i])
s = 0
for i in l:
    s += i // g - 1
print(s)