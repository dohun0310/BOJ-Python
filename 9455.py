for i in range(int(input())):
    m, n = map(int, input().split())
    l = [[0] * n for j in range(m)]
    for j in range(m):
        l[j] = list(map(int, input().split()))
    s = 0
    for j in range(n):
        t = m - 1
        for k in range(m)[::-1]:
            if l[k][j] == 1:
                s += t - k
                t -= 1
    print(s)