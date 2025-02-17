n = int(input())
v = int(input())
l = [0] * n
g = [[] for i in range(n)]
for i in range(v):
    a, b = map(int, input().split())
    g[a - 1] += [b - 1]
    g[b - 1] += [a - 1]
q = [0]
l[0] = 1
while q:
    a = q.pop(0)
    for i in g[a]:
        if not l[i]:
            q.append(i)
            l[i] = 1
print(sum(l) - 1)