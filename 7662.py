import sys
import heapq
t = int(sys.stdin.readline().strip())
for _ in range(t):
    k = int(sys.stdin.readline().strip())
    a, b = [], []
    d = {}
    for _ in range(k):
        o, n = sys.stdin.readline().split()
        n = int(n)
        if o == "I":
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
            heapq.heappush(a, n)
            heapq.heappush(b, -n)
        elif o == "D":
            if n == 1:
                while b and d[-b[0]] == 0:
                    heapq.heappop(b)
                if b:
                    x = -heapq.heappop(b)
                    d[x] -= 1
            elif n == -1:
                while a and d[a[0]] == 0:
                    heapq.heappop(a)
                if a:
                    y = heapq.heappop(a)
                    d[y] -= 1
    while a and d[a[0]] == 0:
        heapq.heappop(a)
    while b and d[-b[0]] == 0:
        heapq.heappop(b)
    if not a or not b:
        print("EMPTY")
    else:
        print(-b[0], a[0])