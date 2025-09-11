a, b, c, m = map(int, input().split())
p = 0
s = 0
for i in range(24):
    if p + a <= m:
        p += a
        s += b
    else:
        p = max(0, p - c)
print(s)