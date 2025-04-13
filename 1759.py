from itertools import combinations
l, c = map(int, input().split())
a = input().split()
s = []
for i in combinations(sorted(a), l):
    t, p = 0, 0
    for j in i:
        if j in "aeiou":
            t += 1
        else:
            p += 1
    if t >= 1 and p >= 2:
        print(*i, sep="")