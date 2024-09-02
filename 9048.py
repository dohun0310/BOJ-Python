for i in range(int(input())):
    f, r, n = map(int, input().split())
    l = [[0] for j in range(f)]
    for j in range(n):
        a, b = map(int, input().split())
        l[a - 1].append(b)
    s = 2 * f + r + 1
    for j in range(f):
        t = 100000
        l[j] += [r + 1]
        l[j].sort()
        for k in range(len(l[j]) - 1):
            t = min(t, l[j][k] + r + 1 - l[j][k + 1])
        s += t * 2
    print(s)