from itertools import permutations
n = int(input())
l = [i for i in range(1, n + 1)]
for i in permutations(l):
    print(*i)