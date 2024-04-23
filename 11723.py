import sys
s = set()
r = int(sys.stdin.readline())
for i in range(r):
    x = sys.stdin.readline().split()
    if x[0] == "add":
        s.add(int(x[1]))
    elif x[0] == "remove":
        s.discard(int(x[1]))
    elif x[0] == "check":
        if int(x[1]) in s:
            print(1)
        else:
            print(0)
    elif x[0] == "toggle":
        if int(x[1]) in s:
            s.discard(int(x[1]))
        else:
            s.add(int(x[1]))
    elif x[0] == "all":
        for i in range(1, 21):
            s.add(i)
    elif x[0] == "empty":
        s = set()