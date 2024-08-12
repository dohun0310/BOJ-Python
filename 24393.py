import sys
from collections import deque
q = deque([1] + [0] * 26)
n = int(sys.stdin.readline())
while n:
    l = list(map(int, sys.stdin.readline().split()))
    a = deque()
    for i in range(13):
        a.append(q.popleft())
    b = deque()
    for i in range(14):
        b.append(q.popleft())
    for i, j in enumerate(l):
        if i % 2:
            for k in range(j):
                q.append(a.popleft())
        else:
            for k in range(j):
                q.append(b.popleft())
    n -= 1
q = list(q)
for i in range(27):
    if q[i]:
        print(i + 1)
        break