import sys
n, m = map(int, sys.stdin.readline().split())
s = {}
for i in range(n):
    a, b = map(str, sys.stdin.readline().split())
    s[a] = b
for i in range(m):
    t = input()
    print(s[t])