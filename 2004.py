n, m = map(int, input().split())
a, b, c = n, n - m, m
x, y, z = n, n - m, m
i, j, k = 0, 0, 0
l, m, n = 0, 0, 0
while a >= 2:
    i += a // 2
    a //= 2
while b >= 2:
    j += b // 2
    b //= 2
while c >= 2:
    k += c // 2
    c //= 2
while x >= 5:
    l += x // 5
    x //= 5
while y >= 5:
    m += y // 5
    y //= 5
while z >= 5:
    n += z // 5
    z //= 5
print(min(i - j - k, l - m - n))