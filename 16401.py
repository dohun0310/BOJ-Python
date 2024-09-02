m, n = map(int, input().split())
l = list(map(int, input().split()))
s, e, a = 1, 1000000000, 0
while s <= e:
    t = (s + e) // 2
    c = 0
    for i in l:
        c += i // t
    if c >= m:
        a = max(a, t)
        s = t + 1
    else:
        e = t - 1
print(a)