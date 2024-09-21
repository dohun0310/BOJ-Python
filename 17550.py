import sys
n = int(sys.stdin.readline())
a = [0] * n
for i in range(n):
    a[i] = int(sys.stdin.readline())
b = [i ** 2 for i in a]
s = 0
for i in range(n - 1):
    a[-(i + 2)] += a[-(i + 1)]
    b[i + 1] += b[i]
for i in range(n - 1):
    s = max(s, b[i] * a[i + 1])
print(s)