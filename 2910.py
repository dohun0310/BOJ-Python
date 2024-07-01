n, c = map(int, input().split())
m = list(map(int, input().split()))
d = {}
c = 1
for i in m:
    if i in d:
        d[i][0] += 1
    else:
        d[i] = [1, c]
        c += 1
m.sort(key=lambda x: (-d[x][0], d[x][1]))
print(*m)