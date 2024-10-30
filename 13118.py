p = list(map(int, input().split()))
x, y, r = map(int, input().split())
if p.count(x) > 0:
    print(p.index(x) + 1)
else:
    print(0)