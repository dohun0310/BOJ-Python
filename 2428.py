n = int(input())
l = sorted(list(map(int, input().split())))
t = 0
for i in range(n - 1):
    s, e = i + 1, n - 1
    a = -1
    while s <= e:
        m = (s + e) // 2
        if l[m] * 0.9 <= l[i]:
            a = m
            s = m + 1
        else:
            e = m - 1
    if a != -1:
        t += a - i
    else:
        t += 0
print(t)