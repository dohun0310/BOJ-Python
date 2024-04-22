import sys
r = int(sys.stdin.readline())
s = 0
for i in range(r):
    n = int(sys.stdin.readline())
    s += n
    if i > 0:
        s -= 1
print(s)