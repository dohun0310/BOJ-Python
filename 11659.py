import sys
n, m = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
s = [0]
c = 0
for i in l:
    c += i
    s.append(c)
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    print(s[b] - s[a - 1])