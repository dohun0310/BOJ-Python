from itertools import product
n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
for i in product(l, repeat=m):
    for j in i:
        print(j, end=" ")
    print()