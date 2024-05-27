n = int(input())
s = 0
c = 0
a = 0
b = 0
while b <= n:
    if s < n:
        b += 1
        s += b
    elif s > n:
        s -= a
        a += 1
    else:
        c += 1
        b += 1
        s += b
print(c)