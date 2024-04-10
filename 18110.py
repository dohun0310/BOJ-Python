import sys

def cround(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)
r = int(sys.stdin.readline())
if r != 0:
    l = []
    for i in range(r):
        l.append(int(sys.stdin.readline()))
    p = cround(r * 0.15)
    l.sort()
    if p > 0:
        print(cround(sum(l[p:-p]) / len(l[p:-p])))
    else:
        print(cround(sum(l) / len(l)))
else:
    print(0)