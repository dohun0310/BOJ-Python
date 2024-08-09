import sys
n = int(sys.stdin.readline())
g = [[] for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    g[a].append(b)
    g[b].append(a)
q = int(sys.stdin.readline())
for i in range(q):
    t, k = map(int, sys.stdin.readline().split())
    if t == 1:
        if len(g[k]) < 2:
            print("no")
        else:
            print("yes")
    elif t == 2:
        print("yes")