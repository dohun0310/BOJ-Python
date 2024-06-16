from itertools import combinations
n, m = map(int, input().split())
l = list(combinations(range(1, n + 1), 3))
s = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    s[a][b] = s[b][a] = 1
c = 0
for i in l:
    if s[i[0]][i[1]] or s[i[1]][i[2]] or s[i[0]][i[2]]:
        continue
    c += 1
print(c)