import sys
n, m = map(int, sys.stdin.readline().split())
l = [[]] * n
for i in range(n):
    l[i] = list(map(int, sys.stdin.readline().split()))
t = [0] * n
s = [0] * m
for i in range(n):
    for j in range(m):
        if s[j] > t[i]:
            s[j] += l[i][j]
        else:
            s[j] = l[i][j] + t[i]
        t[i] = s[j]
print(*t)