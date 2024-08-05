import sys
a, b, c, d = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
s = 0
for i in range(n):
    u, v = map(int, sys.stdin.readline().split())
    fx = max(a * (v - b) ** 2 + c, d)
    if fx == u and b <= v:
        s += 1
print(s)