n = int(input())
l = [[0, 0]] * n
for i in range(n):
    l[i] = list(map(int, input().split()))
l.sort(key=lambda x: (x[0], x[1]))
c = -1
for i in range(n):
    if l[i][0] >= c:
        c = l[i][0] + l[i][1]
    else:
        c += l[i][1]
print(c)