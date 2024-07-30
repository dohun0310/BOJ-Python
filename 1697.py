from collections import deque
def bfs(v, r):
    global s
    q = deque([r])
    while q:
        x = q.popleft()
        if x == k:
            s = v[x]
            break
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= m and not v[nx]:
                v[nx] = v[x] + 1
                q.append(nx)
n, k = map(int, input().split())
m = 10 ** 5
g = [0] * (m + 1)
s = 0
bfs(g, n)
print(s)