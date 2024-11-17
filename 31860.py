import heapq
from collections import deque
n, m, k = map(int, input().split())
l = []
q = deque([0])
for i in range(n):
    heapq.heappush(l, -int(input()))
while l:
    t = -heapq.heappop(l)
    q.append(t + q[-1] // 2)
    t -= m
    if t > k:
        heapq.heappush(l, -t)
q.popleft()
print(len(q))
while q:
    print(q.popleft())