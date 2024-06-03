import sys
from collections import deque
q = deque()
for i in range(int(input())):
    n = sys.stdin.readline().split()
    if n[0] == "push":
        q.append(n[1])
    elif n[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif n[0] == "size":
        print(len(q))
    elif n[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif n[0] == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif n[0] == "back":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])