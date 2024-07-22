import math
t = int(input())
for i in range(t):
    r, b, m = map(float, input().split())
    r = (r + 100.0) / 100.0
    i = 0
    f = False
    p = b
    while i < 1200 and not f:
        b = math.floor((b * r * 100) + 0.5 + 1e-8) / 100.0 - m
        if b <= 0:
            break
        if b > p:
            f = True
        p = b
        i += 1
    if f or i == 1200:
        print("impossible")
    else:
        print(i + 1)