import sys
n, m = [int(i) for i in sys.stdin.readline().split()]
l = [set() for i in range(n)]
s = set()
for i in range(m):
    a = sys.stdin.readline().rstrip()
    if a in s:
        print("NO")
        exit()
    s.add(a)
    for j in a:
        l[a.index(j)].add(j)
h, c, u = set(), 0, 1
for i in l:
    h |= i
    c += len(i)
    u *= len(i)
if c != len(h) or u != m:
    print("NO")
    exit()
print("YES")
for i in l:
    print(*sorted(i), sep="", end="\n")