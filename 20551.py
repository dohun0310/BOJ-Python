import sys
n, m = map(int, sys.stdin.readline().split())
a = [0] * n
for i in range(n):
    a[i] = int(sys.stdin.readline())
a.sort()
d = [0] * m
for i in range(m):
    d[i] = int(sys.stdin.readline())
for i in d:
    s, e = 0, n
    while s < e:
        j = (s + e) // 2
        if i <= a[j]:
            e = j
        else:
            s = j + 1
    if 0 <= s < n and a[s] == i:
        print(s)
    else:
        print(-1)