n = int(input())
p = [[0, 0] for i in range(n)]
for i in range(n):
    p[i] = list(map(int, input().split()))
m = int(input())
l = list(map(int, input().split()))
for i in l:
    p[i - 1] = [0, 0]
for i in range(n):
    for j in l:
        if j in p[i]:
            p[i] = [0, 0]
            continue
c = 0
for i, j in p:
    if i != 0 and j != 0:
        c += 1
print(c)