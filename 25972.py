import sys
n = int(sys.stdin.readline())
l = [[0, 0]] * n
p, c = 0, 0
for i in range(n):
    l[i] = list(map(int, sys.stdin.readline().split()))
for d, l in sorted(l):
    if p < d:
        c += 1
    p = d + l
print(c)