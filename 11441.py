import sys
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
s = [0] * (n + 1)
for i in range(1, n + 1):
    s[i] = l[i- 1] + s[i - 1]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    sys.stdout.write(str(s[b] - s[a - 1]) + "\n")