from collections import deque
n = int(input())
q = deque(enumerate(map(int, input().split())))
s = []
while q:
    i, x = q.popleft()
    s.append(i + 1)
    if x > 0:
        q.rotate(-(x - 1))
    else:
        q.rotate(-x)
print(*s)