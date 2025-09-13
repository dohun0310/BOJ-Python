import sys
n, m = map(int, sys.stdin.readline().rsplit())
l = [[0, 0] for i in range(n)]
for i in range(m):
    k, s, e = map(int, sys.stdin.readline().rsplit())
    if s >= l[k - 1][1]:
        print("YES")
        l[k - 1] = [s, e]
    else:
        print("NO")