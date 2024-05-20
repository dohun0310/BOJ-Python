import sys
n = int(sys.stdin.readline().strip())
h = sorted(list(map(int, sys.stdin.readline().strip().split())))
m = int(sys.stdin.readline().strip())
d = list(map(int, sys.stdin.readline().strip().split()))
s = {}
for i in h:
    if i in s:
        s[i] += 1
    else:
        s[i] = 1
for i in d:
    if i in s:
        print(s[i], end=" ")
    else:
        print(0, end=" ")