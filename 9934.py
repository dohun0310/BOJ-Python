k = int(input())
l = list(map(int,input().split()))
s = [(0, len(l) - 1, 0)]
a = [[] for i in range(len(l))]
while s:
    i, j, d = s.pop()
    if i == j:
        a[d].append(l[i])
    else:
        m = (i + j) // 2
        a[d].append(l[m])
        s.append((i, m - 1, d + 1))
        s.append((m + 1, j, d + 1))
for i in a:
    i.reverse()
    print(*i)