from collections import deque
q = deque(i for i in range(1, int(input()) + 1))
l = []
while len(q) > 1:
    l.append(q.popleft())
    q.append(q.popleft())
print(*l, end=" ", *q)