n, k = map(int, input().split())
l = [0] * (n + 1)
c = 0
for i in range(2, n + 1):
    if l[i] == 0:
        for j in range(i, n + 1, i):
            if l[j] == 0:
                l[j] = 1
                c += 1
                if c == k:
                    print(j)