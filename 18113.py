import sys
n, k, m = map(int, sys.stdin.readline().split())
l = []
for i in range(n):
    g = int(sys.stdin.readline().rstrip())
    if g > k * 2:
        l.append(g - (2 * k))
    elif g - k > 0 and g < 2 * k:
        l.append(g - k)
if len(l) == 0:
    print(-1)
    exit()
s, e, p = 1, max(l), -1
while s <= e:
    t = (s + e) // 2
    a = sum([i // t for i in l])
    if a < m:
        e = t - 1
    else:
        s = t + 1
        p = t
print(p)