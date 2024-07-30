n = int(input())
l = [[0, 0]] * n
for i in range(n):
    l[i] = list(map(int, input().split()))
l.sort(key=lambda x: [x[1], x[0]])
e = 0
c = 0
for i, j in l:
    if i >= e:
        c += 1
        e = j
print(c)