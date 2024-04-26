t = int(input())
for i in range(t):
    k = int(input())
    n = int(input())
    s = [j for j in range(1, n + 1)]
    for l in range(k):
        for m in range(1, n):
            s[m] += s[m - 1]
    print(s[-1])