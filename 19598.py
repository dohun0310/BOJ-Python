n = int(input())
l = []
for i in range(n):
    s, e = map(int, input().split())
    l.append([s, 1])
    l.append([e, -1])
l.sort()
r = 0
c = 0
for i, j in l:
    c += j
    r = max(c, r)
print(r)