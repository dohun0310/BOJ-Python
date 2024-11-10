m = int(input())
l = [0] * m
for i in list(map(float, input().split())):
    d = i
    d += 1e-9
    l[m * int(d * 1000000) // 1000000] += 1
for i in range(m):
    print(l[i], end=" ")