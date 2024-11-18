import sys
import heapq
t, a, b = map(int, sys.stdin.readline().split())
l = [[False] * 2 for i in range(5000050)]
s = 0
q = []
heapq.heappush(q, (-1, a))
heapq.heappush(q, (-1, b))
while q:
    c, p = heapq.heappop(q)
    c = -c
    if p > t:
        continue
    l[p][c] = True
    s = max(s, p)
    if c and not l[p // 2][0]:
        heapq.heappush(q, (0, p // 2))
    if t - p >= a:
        heapq.heappush(q, (-c, p + a * ((t - p) // a)))
    if t - p >= b:
        heapq.heappush(q, (-c, p + b * ((t - p) // b)))
print(s)