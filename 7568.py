n = int(input())
l = [[0, 0]] * n
for i in range(n):
    l[i] = list(map(int, input().split()))
for i in l:
    s = 1
    for j in l:
        if i[0] < j[0] and i[1] < j[1]:
            s += 1
    print(s, end=" ")