for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    m = int(input())
    s = [[0] * (m + 1) for j in range(n + 1)]
    for j in range(n + 1):
        s[j][0] = 1
    for j in range(1, n + 1):
        for k in range(1, m + 1):
            s[j][k] = s[j - 1][k]
            if k >= l[j - 1]:
                s[j][k] += s[j][k - l[j - 1]]
    print(s[n][m])