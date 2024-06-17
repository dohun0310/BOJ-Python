from itertools import combinations
n, m = map(int, input().split())
l = sorted(list(map(int, input().split())))
for i in combinations(l, m):
    print(*i)