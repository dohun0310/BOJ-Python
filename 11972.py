n, m, d, s = map(int, input().split())
a = [[] for i in range(n)]
l = [0] * (m + 1)
for i in range(d):
    p, m, t = map(int, input().split())
    a[p - 1].append((m, t))
for i in range(s):
    p, t = map(int, input().split())
    for j in a[p - 1]:
        if j[1] < t:
            l[j[0]] += 1
p = 0
for i in range(len(l)):
    if l[i] < s:
        continue
    t = 0
    for j in a:
        for k in j:
            if k[0] == i:
                t += 1
                break
    p = max(p, t)
print(p)