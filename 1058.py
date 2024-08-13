n = int(input())
l = []
for i in range(n):
    l.append(list(input()))
g = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            if j == k:
                continue
            if l[j][k] == "Y" or (l[j][i] == "Y" and l[i][k] == "Y"):
                g[j][k] = 1
s = 0
for i in g:
    s = max(s, sum(i))
print(s)