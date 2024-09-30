import sys
n, m, q = map(int, sys.stdin.readline().split())
e = [0] * m
for i in range(m):
    e[i] = int(sys.stdin.readline())
for i in range(q):
    s = list(map(str, sys.stdin.readline().split()))
    x, y = s[0], list(map(int, s[1:]))
    if x == "assign":
        e[y[0] - 1] = e[y[1] - 1]
    elif x == "swap":
        e[y[0] - 1], e[y[1] - 1] = e[y[1] - 1], e[y[0] - 1]
    else:
        e[y[0] - 1] = 0
e = sorted(list(set(e)))
e.remove(0)
print(len(e))
if len(e):
    print(*e, sep="\n")