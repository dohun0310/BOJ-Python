n, m = map(int, input().split())
a = list(map(int, input().split()))
l, r, c, s = 0, 0, a[0], 0
while True:
    if c == m:
        s += 1
        c -= a[l]
        l += 1
    elif c < m:
        r += 1
        if r == n:
            break
        c += a[r]
    else:
        c -= a[l]
        l += 1
print(s)