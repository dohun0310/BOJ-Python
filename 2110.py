n, c = map(int, input().split())
l = [0] * n
for i in range(n):
    l[i] = int(input())
l.sort()
r, s, e = 0, 1, l[-1] - l[0]
while s <= e:
    m = (s + e) // 2
    u, p = 1, l[0]
    for i in range(1, len(l)):
        if l[i] >= p + m:
            u += 1
            p = l[i]
    if u >= c:
        s = m + 1
        r = m
    else:
        e = m - 1
print(r)