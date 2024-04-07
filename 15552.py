import sys
r = int(sys.stdin.readline())
for i in range(1, r + 1):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)