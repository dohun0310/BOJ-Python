n, k = map(int, input().split())
l = [0] * n
for i in range(n):
    l[i] = int(input())
l.sort()
s = l[0]
e = s + k
r = 0
while s <= e:
    m = (s + e) // 2
    c = 0
    for i in l:
        if m > i:
            c += m - i
    if c <= k:
        s = m + 1
        r = m
    else:
        e = m - 1
print(r)