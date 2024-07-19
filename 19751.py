import itertools
a, b, c, d = map(int, input().split())
l = [a, b, c, d]
print(*min(itertools.permutations(l), key=lambda x: x[0] / x[1] + x[2] / x[3]), sep=" ")