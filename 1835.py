from collections import deque
n = int(input())
s = deque([n])
for i in range(1, n)[::-1]:
    s.appendleft(i)
    for j in range(i):
        s.appendleft(s.pop())
print(*s)