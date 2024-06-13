import sys
import heapq
q = []
n = int(sys.stdin.readline())
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q))
    else:
        heapq.heappush(q, x)