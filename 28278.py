import sys
from collections import deque
q = []
for i in range(int(input())):
    n = sys.stdin.readline().split()
    if n[0] == "1":
        q.append(n[1])
    elif n[0] == "2":
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop())
    elif n[0] == "3":
        print(len(q))
    elif n[0] == "4":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif n[0] == "5":
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])