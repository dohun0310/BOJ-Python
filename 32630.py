n = int(input())
l = list(map(int, input().split()))
s = sum(l)
u = [2 * i - 1 for i in l]
u.sort()
a = u[0] * u[1]
b = u[-1] * u[-2]
if b > a:
    c = b
else:
    c = a
if c > 1:
    t = (c - 1) // 2
else:
    t = 0
print(s + t)