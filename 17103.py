p = [1] * 1000001
for i in range(2, 1000001):
    if p[i]:
        for j in range(2 * i, 1000001, i):
            p[j] = 0
for i in range(int(input())):
    n = int(input())
    c = 0
    for j in range(2, n // 2 + 1):
        if p[j] and p[n - j]:
            c += 1
    print(c)