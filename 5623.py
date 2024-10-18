n = int(input())
l = [[]] * n
for i in range(n):
    l[i] = list(map(int, input().split()))
if n == 2:
    print(1, 1)
else:
    t = [(l[0][1] + l[0][2] - l[1][2]) // 2]
    for i in range(1, n):
        t.append(l[i][0] - t[0])
    print(*t)