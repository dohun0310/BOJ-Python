import heapq
t = int(input())
l = []
for i in range(t):
    heapq.heappush(l, int(input()))
s = 0
while len(l) > 1:
    a = heapq.heappop(l)
    b = heapq.heappop(l)
    s += a + b
    heapq.heappush(l, a + b)
print(s)