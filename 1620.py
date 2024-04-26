import sys
n, m = map(int, sys.stdin.readline().split())
a = {}
b = {}
for i in range(1, n + 1):
    s = sys.stdin.readline().strip()
    a[i] = s
    b[s] = i
for i in range(m):
    s = sys.stdin.readline().strip()
    if s.isdigit():
        print(a[int(s)])
    else:
        print(b[s])