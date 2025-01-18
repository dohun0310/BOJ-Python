l = [[0] * 100 for i in range(100)]
for i in range(int(input())):
    x, y = map(int, input().split())
    for j in range(x, x + 10):
        for k in range(y, y + 10):
            l[j][k] = 1
print(sum(sum(l, [])))