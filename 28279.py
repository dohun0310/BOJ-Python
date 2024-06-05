import sys
from collections import deque
q = deque()
n = int(sys.stdin.readline())
for i in range(n):
    s = sys.stdin.readline().split()
    if s[0] == "1":
        q.appendleft(s[1])
    elif s[0] == "2":
        q.append(s[1])
    elif s[0] == "3":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif s[0] == "4":
        if q:
            print(q.pop())
        else:
            print(-1)
    elif s[0] == "5":
        print(len(q))
    elif s[0] == "6":
        if q:
            print(0)
        else:
            print(1)
    elif s[0] == "7":
        if q:
            print(q[0])
        else:
            print(-1)
    elif s[0] == "8":
        if q:
            print(q[-1])
        else:
            print(-1)