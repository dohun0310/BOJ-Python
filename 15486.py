import sys
n = int(sys.stdin.readline())
t, p = [0] * n, [0] * n
for i in range(n):
    t[i], p[i] = map(int, sys.stdin.readline().split())
l = [0] * (n + 1)
for i in range(n):
    l[i] = max(l[i], l[i - 1])
    if i + t[i] <= n:
        l[i + t[i]] = max(l[i + t[i]], l[i] + p[i])
print(max(l))