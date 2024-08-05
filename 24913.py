import sys
n, q = map(int, sys.stdin.readline().split())
l = [0] * (n + 2)
m = 0
s = 0
for i in range(q):
    t, x, y = map(int, sys.stdin.readline().split())
    if t == 1:
        l[y] += x
        if y != n + 1:
            s += x
            if l[y] > m:
                m = l[y]
    else:
        if m < l[n + 1] + x and s + y <= n * (l[n + 1] + x - 1):
            print("YES")
        else:
            print("NO")