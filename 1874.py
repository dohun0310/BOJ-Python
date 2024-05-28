n = int(input())
l = [0] * n
s = []
g = []
c = 1
a = 1
for i in range(n):
    l[i] = int(input())
for i in l:
    while c <= i:
        g.append("+")
        s.append(c)
        c += 1
    if s[-1] > i:
        a = 0
    if s[-1] == i:
        g.append("-")
        s.pop()
if a:
    for i in g:
        print(i)
else:
    print("NO")