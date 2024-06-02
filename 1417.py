n = int(input())
l = [0] * n
for i in range(n):
    l[i] = int(input())
d = l[0]
l.remove(l[0])
c = 0
if n == 1:
    print(0)
else:
    while max(l) >= d:
        d += 1
        l[l.index(max(l))] -= 1
        c += 1
    print(c)