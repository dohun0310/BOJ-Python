import math
n, s = map(int, input().split())
a = list(map(int, input().split()))
l = []
for i in a:
    l.append(abs(s - i))
s = l[0]
for i in l[1:]:
    s = math.gcd(s, i)
print(s)