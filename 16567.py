import sys
n, m = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))
c = 0
e = 0
for i in range(n):
    if s[i] == 0:
        e = 0
    elif s[i] == 1:
        if e == 0:
            c += 1
            e = 1
for i in range(m):
    a = list(map(int, sys.stdin.readline().split()))
    if a[0] == 1 and s[a[1] - 1] == 0:
        a[1] -= 1
        if a[1] == 0:
            if s[1] == 0:
                c += 1
                s[a[1]] = 1
        elif a[1] == n - 1:
            if s[n - 2] == 0:
                c += 1
                s[a[1]] = 1
        else:
            if s[a[1] - 1] == 1 and s[a[1] + 1] == 1:
                c -= 1
                s[a[1]] = 1
            elif s[a[1] - 1] == 0 and s[a[1] + 1] == 0:
                s[a[1]] = 1
                c += 1
            else:
                s[a[1]] = 1
    elif a[0] == 0:
        print(c)