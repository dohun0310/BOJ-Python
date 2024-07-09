from itertools import combinations
n, m = map(int, input().split())
l = list(map(int, input().split()))
for i in sorted(set(combinations(sorted(l), m))):
    print(*i, sep=" ")