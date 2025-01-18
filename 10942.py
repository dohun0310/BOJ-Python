import sys
n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
l = [[0] * n for i in range(n)]
for i in range(n):
    l[i][i] = 1
for i in range(n - 1):
    if m[i] == m[i + 1]:
        l[i][i + 1] = 1
for i in range(n - 2):
    for j in range(n - 2 - i):
        t = j + i + 2
        if m[j] == m[t] and l[j + 1][t - 1]:
            l[j][t] = 1
for i in range(int(sys.stdin.readline())):
    s, e = map(int, sys.stdin.readline().split())
    print(l[s - 1][e - 1])