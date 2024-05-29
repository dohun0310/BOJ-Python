import sys
n = int(sys.stdin.readline())
l = [0] * n
for i in range(n):
    l[i] = int(sys.stdin.readline())
l.sort(reverse=True)
for i in l:
    print(i)