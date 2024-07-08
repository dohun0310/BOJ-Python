import sys
from collections import deque
n = int(input())
a = [[0] for i in range(n + 1)]
b = [0] * (n + 1)
for i in range(n - 1):
    x, y = map(int, sys.stdin.readline().split())
    a[x].append(y)
    a[y].append(x)
q = deque()
q.append(1)
while q:
    x = q.popleft()
    for i in a[x]:
        if b[i] == 0:
            b[i] = x
            q.append(i)
for i in range(2, n + 1):
    print(b[i])