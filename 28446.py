import sys
d = {}
for i in range(int(sys.stdin.readline())):
    l = list(map(int, sys.stdin.readline().split()))
    if l[0] == 1:
        d[l[2]] = l[1]
    else:
        print(d[l[1]])