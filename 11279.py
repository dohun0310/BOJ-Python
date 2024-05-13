import sys
import heapq
n = int(sys.stdin.readline())
l = []
for i in range(n):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(l, -x)
    else:
        if len(l):
            t = heapq.heappop(l)
            print(-t)
        else:
            print(0)