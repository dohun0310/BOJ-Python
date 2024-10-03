import sys
n = int(sys.stdin.readline())
l = []
x, y = 0, 0
for i in range(n):
    a = list(map(int, sys.stdin.readline().split()))
    if a[0] == 1:
        l.append(a[1])
    else:
        l.pop()
    if x < len(l):
        x = len(l)
        y = l[-1]
    elif x == len(l):
        y = min(y, l[-1])
print(x, y)