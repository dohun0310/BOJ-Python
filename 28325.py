import sys
n = int(sys.stdin.readline())
c = list(map(int, sys.stdin.readline().split()))
s = set()
for i in range(n):
    if c[i] != 0:
        s.add(i)
if len(s) == 0:
    print(n // 2)
else:
    m = [-1] * n
    u = 0
    for i in range(n):
        if i in s:
            u += c[i]
            m[i] = 0
    if n == 2:
        if len(s) == 1:
            u += 1
        print(u)
    else:
        t = 0
        for i in range(n):
            if i in s:
                t = i
                break
        for i in range(t, n + t):
            if m[i % n] == -1:
                if m[(i - 1) % n] != 1 and m[(i + 1) % n] != 1:
                    m[i % n] = 1
                    u += 1
        print(u)