import sys
n, t = map(int, input().split())
s = input()
m = []
for i in range(t):
    m.append(tuple(map(int, sys.stdin.readline().split())))
m.sort()
c = 0
l = [1000, 0]
for i in range(n):
    if s[i] == "0":
        continue
    f = False
    v = []
    for j in range(252):
        a = [0] * (n + 1)
        a[i + 1] = 1
        d = {}
        if j != 0:
            d[i + 1] = j
            for p in range(t):
                x, y = m[p][1], m[p][2]
                if x in d and y in d:
                    d[x] -= 1
                    d[y] -= 1
                    if d[x] <= 0:
                        del d[x]
                    if d[y] <= 0:
                        del d[y]
                elif x in d:
                    if a[y] == 0:
                        d[y] = j
                        a[y] = 1
                    d[x] -= 1
                    if d[x] <= 0:
                        del d[x]
                elif y in d:
                    if a[x] == 0:
                        d[x] = j
                        a[x] = 1
                    d[y] -= 1
                    if d[y] <= 0:
                        del d[y]
        if "".join(map(str, a[1:])) == s:
            f = True
            v.append(j)
    if f:
        c += 1
        l = [min(l[0], min(v)), max(l[1], max(v))]
print(c, end=" ")
print("Infinity" if l[0] == 251 else l[0], end=" ")
print("Infinity" if l[1] == 251 else l[1])