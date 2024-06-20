from itertools import permutations
n, m = map(int, input().split())
l = list(map(int, input().split()))
for i in sorted(set(permutations(l, m))):
    print(*i)