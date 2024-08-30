import sys
n, m, k = map(int, sys.stdin.readline().split())
c = 0
x = 1
for i in range(m):
    t, r = map(int, sys.stdin.readline().split())
    if x:
        c += r
        if c > k:
            print(f"{i + 1} 1")
            x = 0
if x:
    print(-1)