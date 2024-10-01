import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
x, y = b[b.index(a[0]):] + b[:b.index(a[0])], b[b.index(a[0]) + 1:] + b[:b.index(a[0]) + 1]
if a == x or a == y[::-1]:
    print("good puzzle")
else:
    print("bad puzzle")