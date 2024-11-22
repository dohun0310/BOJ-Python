import bisect
for i in range(int(input())):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    c = 0
    for j in a:
        c += (bisect.bisect(b, j - 1))
    print(c)