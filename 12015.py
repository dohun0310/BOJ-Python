def b(x):
    s, e = 0, len(l) - 1
    while s <= e:
        m = (s + e) // 2
        if l[m] == x:
            return m
        elif l[m] < x:
            s = m + 1
        else:
            e = m - 1
    return s
n = int(input())
a = list(map(int, input().split()))
l = [a[0]]
for i in range(n):
    if a[i] > l[-1]:
        l.append(a[i])
    else:
        l[b(a[i])] = a[i]
print(len(l))