n, m = map(int, input().split())
c = 0
while True:
    if n == m:
        c += 1
        break
    elif n > m:
        n = n - m
        c += 1
    elif m > n:
        m = m - n
        c += 1
print(c)