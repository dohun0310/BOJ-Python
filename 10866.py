import sys
r = int(sys.stdin.readline())
l = []
for i in range(r):
    a = list(map(str, sys.stdin.readline().split()))
    if a[0] == "push_front":
        l.insert(0, a[1])
    elif a[0] == "push_back":
        l.append(a[1])
    elif a[0] == "pop_front":
        if len(l) != 0:
            print(l.pop(0))
        else:
            print(-1)
    elif a[0] == "pop_back":
        if len(l) != 0:
            print(l.pop())
        else:
            print(-1)
    elif a[0] == "size":
        print(len(l))
    elif a[0] == "empty":
        if len(l) == 0:
            print(1)
        else:
            print(0)
    elif a[0] == "front":
        if len(l) != 0:
            print(l[0])
        else:
            print(-1)
    elif a[0] == "back":
        if len(l) != 0:
            print(l[-1])
        else:
            print(-1)