import sys
t = int(sys.stdin.readline())
l = []
c = 1
for i in range(t):
    n = int(sys.stdin.readline())
    c += 1
    s = 0
    q = []
    while n > 0:
        s *= 3
        if n % 2 == 1:
            q.append(1)
        else:
            q.append(0)
        n //= 2
    h = 1
    while q:
        s += q.pop(0) * h
        h *= 3
    l.append(s)
print(*l, sep="\n")