from itertools import product
n, m = map(int, input().split())
l = list(map(int, input().split()))
for i in sorted(set(product(sorted(l), repeat=m))):
    print(*i, sep=" ")