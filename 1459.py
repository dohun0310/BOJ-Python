x, y, w, s = map(int, input().split())
if (x + y) % 2 == 0:
    print(min((x + y) * w, max(x, y) * s, (min(x, y) * s) + (abs(x-y) * w)))
else:
    print(min((x + y) * w, (max(x, y) - 1) * s + w, (min(x, y) * s) + (abs(x - y) * w)))