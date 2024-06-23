import heapq
n = int(input())
l = list(map(int, input().split()))
c = 0
s = []
for i in l:
    if i > 1440:
        print(-1)
        exit(0)
    else:
        heapq.heappush(s, -i)
while len(s) > 1:
    m = -heapq.heappop(s)
    n = -heapq.heappop(s) if s else 0
    heapq.heappush(s, -(m - n))
    c += n
c += -heapq.heappop(s) if s else 0
print(-1 if c > 1440 else c)