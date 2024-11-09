import sys
n = int(sys.stdin.readline())
c = {}
d = {}
x, y = [], []
for i in range(n):
    a,b = map(int , sys.stdin.readline().split(" "))
    x.append(a)
    y.append(b)
    if a in c:
        c[a].append(b)
    else:
        c[a] = []

    if b in d:
        d[b].append(a)
    else:
        d[b] = []
x, y = list(set(x)), list(set(y))
s = 0
for i in x:
    if c[i]:
        s += 1
for i in y:
    if d[i]:
        s += 1
print(s)