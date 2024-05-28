import sys
n = int(sys.stdin.readline())
l = [0] * n
for i in range(n):
    l[i] = int(sys.stdin.readline())
l.sort()
print(round(sum(l) / n))
print(l[n // 2])
c = dict()
for i in l:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
s = []
for i in c:
    if c[i] == max(c.values()):
        s.append(i)
if len(s) == 1:
    print(s[0])
else:
    print(s[1])
print(max(l) - min(l))