import sys
r = int(sys.stdin.readline())
l = []
for i in range(r):
    l.append(int(sys.stdin.readline()))
l.sort()
for i in l:
    print(i)