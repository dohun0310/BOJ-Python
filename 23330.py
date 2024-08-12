import sys
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
l.sort()
a, s = 0, 0
for i in range(n):
    s += abs(l[i] - l[0])
a += s
for i in range(1, n):
    t = l[i] - l[i - 1]
    a += s + (t * i) - (t * (n - i))
    s = s + (t * i) - (t * (n - i))
print(a)