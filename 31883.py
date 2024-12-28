s = 0
for i in range(int(input())):
    a, b, c, d = map(int, input().split())
    t = c + d
    n = t - s % t
    if t - n < c:
        s += a
    elif a + n < b:
        s += a + n
    else:
        s += b
print(s)