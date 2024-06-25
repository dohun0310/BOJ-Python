from collections import deque
n, m = map(int, input().split())
l = list(map(int, input().split()))
q = deque([i for i in range(1, n+1)])
c = 0
for i in l:
    while True:
        if q[0] == i:
            q.popleft()
            break
        else:
            if q.index(i) <= len(q) // 2:
                while q[0] != i:
                    q.append(q.popleft())
                    c += 1
            else:
                while q[0] != i:
                    q.appendleft(q.pop())
                    c += 1
print(c)