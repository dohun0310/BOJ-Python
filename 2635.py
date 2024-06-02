n = int(input())
l = []
for i in range(n, 0, -1):
    s = [n]
    s.append(i)
    j = 1
    while True:
        m = s[j - 1] - s[j]
        if m < 0:
            break
        s.append(m)
        j += 1
    if len(s) > len(l):
        l = s
print(len(l))
print(*l, end=" ")