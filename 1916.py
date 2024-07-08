import sys
import heapq
n = int(input())
m = int(input())
a = [[] for i in range(n + 1)]
for i in range(m):
    x, y, c = map(int, sys.stdin.readline().split())
    a[x].append([y, c])
s, e = map(int, input().split())
d = [1e9] * (n + 1)
h = []
heapq.heappush(h, [0, s])
d[s] = 0
while h:
    c, x = heapq.heappop(h)
    if d[x] < c:
        continue
    for y, nc in a[x]:
        if d[y] > c + nc:
            d[y] = c + nc
            heapq.heappush(h, [d[y], y])
print(d[e])