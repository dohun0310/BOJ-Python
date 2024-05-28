from collections import deque
n = int(input())
for i in range(n):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))
    s = deque(range(0, n))
    c = 0
    while q:
        if q[0] == max(q):
            c += 1
            q.popleft()
            if s.popleft() == m:
                print(c)
                break
        else:
            q.rotate(-1)
            s.rotate(-1)