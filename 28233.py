from collections import deque
n, s, e = map(int, input().split())
n = n * 2
v = [-1] * (n + 1)
v[s] = 0
q = deque([s])
while q:
    t = q.popleft()
    if t == e:
        print(v[t])
        break
    if t <= n // 2:
        p = 2 * t - 1
    else:
        p = 2 * t - n
    if v[p] == -1:
        v[p] = v[t] + 1
        q.append(p)
    if t % 2 == 0:
        p = t - 1
    else:
        p = t + 1
    if v[p] == -1:
        v[p] = v[t] + 1
        q.append(p)
else:
    print(-1)