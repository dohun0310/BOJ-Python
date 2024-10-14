import sys
import math
n = int(sys.stdin.readline())
l = []
c = 1
for i in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))
    c += 2
t = math.inf
a = 0
b = 0
for i in range(1, 101):
    for j in range(1, 101):
        r = 0
        for m, n in l:
            u = m * i + j - n
            r += u * u
        if r < t:
            t = r
            a = i
            b = j
print(a, b)