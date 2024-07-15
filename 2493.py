import sys
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
s = []
a = [0] * n
for i in range(n):
    while s:
        if s[-1][1] > l[i]:
            a[i] = s[-1][0] + 1
            break
        else:
            s.pop()
    if not s:
        a[i] = 0
    s.append([i, l[i]])
print(*a)