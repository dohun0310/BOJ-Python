n, m, k = map(int, input().split())
s = 1
a, b = m, n
t = 10 ** 9 + 7
while b:
    if b % 2:
        s = s * a % t
    a = a * a % t
    b //= 2
if k == 1 or n < k:
    print(s)
elif n > k:
    s = 1
    a, b = m, k % 2 + 1
    while b:
        if b % 2:
            s = s * a % t
        a = a * a % t
        b //= 2
    print(s)
else:
    s = 1
    a, b = m, (n + 1) // 2
    while b:
        if b % 2:
            s = s * a % t
        a = a * a % t
        b //= 2
    print(s)