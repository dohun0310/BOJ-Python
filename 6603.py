from itertools import combinations
while True:
    l = list(map(int, input().split()))
    k = l[0]
    s = l[1:]
    for i in combinations(s, 6):
        print(*i)
    if k == 0:
        exit()
    print()