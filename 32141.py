n, h = map(int, input().split())
d = list(map(int, input().split()))
s = 0
for i in range(n):
    if h <= 0:
        break
    h -= d[i]
    s += 1
if h <= 0:
    print(s)
else:
    print(-1)