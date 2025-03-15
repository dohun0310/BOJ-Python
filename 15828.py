import sys
from collections import deque
n, q = int(sys.stdin.readline()), deque()
while True:
    a = int(sys.stdin.readline())
    if a == -1:
        break
    if a == 0:
        q.popleft()
    elif len(q) < n:
        q.append(a)
if q:
    print(*q)
else:
    print("empty")