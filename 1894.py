import sys
while True:
    try:
        a, b, c, d, e, f, g, h = map(float, sys.stdin.readline().split())
        x, y = 0, 0
        if a == e and b == f:
            x, y = g + c - a, h + d - b
        elif a == g and b == h:
            x, y = e + c - a, f + d - b
        elif c == e and d == f:
            x, y = g + a - c, h + b - d
        elif c == g and d == h:
            x, y = e + a - c, f + b - d
        if x != 0 or y != 0:
            print(f"{x:.3f} {y:.3f}")
    except:
        break