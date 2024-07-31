import sys
from collections import deque
x = int(sys.stdin.readline())
q = deque([(x, 0)])
v = {}
while q:
    k, c = q.popleft()
    if k == 1:
        break
    if k % 3 == 0:
        if k // 3 not in v:
            v[k // 3] = c + 1
            q.append((k // 3, c + 1))
    if k % 2 == 0:
        if k // 2 not in v:
            v[k // 2] = c + 1
            q.append((k // 2, c + 1))
    if k - 1 not in v:
        v[k - 1] = c + 1
        q.append((k - 1, c + 1))
print(c)