n, m = map(int, input().split())
f = [input().split(".") for i in range(n)]
l = set(input() for i in range(m))
f.sort(key=lambda x: (x[0], x[1]))
for i in range(n - 1):
    if f[i][0] == f[i + 1][0]:
        if f[i][1] not in l and f[i + 1][1] in l:
            a = f[i]
            f[i] = f[i + 1]
            f[i + 1] = a
for i in f:
    print(".".join(i))