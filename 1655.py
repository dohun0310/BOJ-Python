import sys, heapq
n = int(sys.stdin.readline())
l, r = [], []
for i in range(n):
    t = int(sys.stdin.readline())
    if len(l) == len(r):
        heapq.heappush(l, -t)
    else:
        heapq.heappush(r, t)
    if r and -l[0] > r[0]:
        heapq.heappush(l, -heapq.heappop(r))
        heapq.heappush(r, -heapq.heappop(l))
    print(-l[0])