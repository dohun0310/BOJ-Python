def b(k, l, r):
    c = 0
    while l <= r:
        m = (l + r) // 2
        if k == m:
            break
        elif k < m:
            r = m - 1
        else:
            l = m + 1
        c += 1
    return c

def t(k, l, r):
    c = 0
    while l <= r:
        a = l + (r - l) // 3
        p = r - (r - l) // 3

        if k == a:
            break
        else:
            c += 1
            if k == p:
                break
            else:
                c += 1
                if k < a:
                    r = a - 1
                elif k < p:
                    l = a + 1
                    r = p - 1
                else:
                    l = p + 1
    return c

n = int(input())
x = 0
y = 0
z = 0
for i in range(n):
    d = b(i, 0, n - 1)
    e = t(i, 0, n - 1)
    if d < e:
        x += 1
    elif d == e:
        y += 1
    else:
        z += 1
print(x)
print(y)
print(z)