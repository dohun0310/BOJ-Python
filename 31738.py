n, m = map(int, input().split())
if n >= m:
    print(0)
else:
    r = 1
    for i in range(2, n + 1):
        r = (r * i) % m
    print(r)