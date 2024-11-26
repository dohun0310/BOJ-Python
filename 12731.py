import sys, heapq
for i in range(1, int(sys.stdin.readline()) + 1):
	t = int(sys.stdin.readline())
	n, m = map(int, sys.stdin.readline().split())
	l = []
	for j in range(n):
		a, b = sys.stdin.readline().split()
		a = tuple(map(int, a.split(":")))
		b = tuple(map(int, b.split(":")))
		l.append((a, b, 0))
	for j in range(m):
		a, b = sys.stdin.readline().split()
		a = tuple(map(int, a.split(":")))
		b = tuple(map(int, b.split(":")))
		l.append((a, b, 1))
	l.sort()
	u = [[], []]
	c = [0, 0]
	for j, h, k in l:
		if u[k] and u[k][0] <= j:
			heapq.heappop(u[k])
			heapq.heappush(u[(k + 1) % 2], (h[0] + 1, h[1] + t - 60) if h[1] + t >= 60 else (h[0], h[1] + t))
		else:
			heapq.heappush(u[(k + 1) % 2], (h[0] + 1, h[1] + t - 60) if h[1] + t >= 60 else (h[0], h[1] + t))
			c[k] += 1
	print(f"Case #{i}: {c[0]} {c[1]}")