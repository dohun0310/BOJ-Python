import heapq
n = int(input())
q = []
for i in range(n):
    for j in list(map(int, input().split())):
        if len(q) < n:
            heapq.heappush(q, j)
        else:
            if q[0] < j:
                heapq.heappop(q)
                heapq.heappush(q, j)
print(q[0])