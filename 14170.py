import sys
import bisect
n, q = map(int, sys.stdin.readline().split())
l = sorted(list(map(int, sys.stdin.readline().split())))
r = []
for i in range(q):
    a, b = map(int, sys.stdin.readline().split())
    r.append(bisect.bisect_right(l, b) - bisect.bisect_left(l, a))
print(*r, sep="\n")