import sys
from itertools import product
n, k = map(int, sys.stdin.readline().split())
l = [""] * n
for i in range(n):
    l[i] = sys.stdin.readline()
a = 0
for i in product("TF", repeat=k):
    i = "".join(i)
    b = float("inf")
    for j in l:
        b = min(b, sum(1 for m in range(k) if j[m] == i[m]))
    a = max(a, b)
print(a)