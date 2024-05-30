import sys
n = int(sys.stdin.readline())
l = dict()
for i in range(n):
    p, o = sys.stdin.readline().rstrip().split()
    if o == "enter":
        l[p] = o
    elif o == "leave":
        del l[p]
for i in sorted(l.keys(), reverse=True):
    print(i)