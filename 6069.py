n, m = map(int, input().split())
l = [0] * n
for _ in range(m):
    o, s, e = map(int, input().split())
    if o == 0:
        for i in range(s - 1, e):
            l[i] = 1 - l[i]
    else:
        c = 0
        for i in range(s - 1, e):
            c += l[i]
        print(c)