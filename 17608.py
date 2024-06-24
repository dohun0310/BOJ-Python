import sys
n = int(sys.stdin.readline())
l = [0] * n
for i in range(n):
    l[i] = int(sys.stdin.readline())
c, m = 0, 0
for i in reversed(l):
    if m < i:
        c += 1
        m = i
print(c)