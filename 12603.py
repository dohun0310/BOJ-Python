from itertools import combinations
for i in range(int(input())):
    c = int(input())
    l = int(input())
    p = list(map(int, input().split()))
    s = []
    for j in range(1, l + 1):
        for k in combinations(p, j):
            if sum(k) == c:
                for m in k:
                    s.append(p.index(m) + 1)
                    p[p.index(m)] = 0
                s.sort()
                print("Case #%d: %s" % (i + 1, " ".join(map(str, s))))
                break
        else:
            continue
        break