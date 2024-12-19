for i in range(int(input())):
    n, m = map(int, input().split())
    l = [[0, 0] for i in range(n)]
    s = []
    for j in range(m):
        a, b, p, q = map(int, input().split())
        l[a - 1][0] += p
        l[a - 1][1] += q
        l[b - 1][0] += q
        l[b - 1][1] += p
    for j in range(n):
        if l[j][0] == 0 and l[j][1] == 0:
            s.append(0)
        else:
            s.append(1000 * l[j][0] ** 2 / (l[j][0] ** 2 + l[j][1] ** 2))
    print(int(max(s)), int(min(s)))