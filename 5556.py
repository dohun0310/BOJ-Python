n = int(input())
k = int(input())
l = [[]] * k
for i in range(k):
    l[i] = list(map(int, input().split()))
for i, j in l:
    if i > (n + 1) / 2:
        i = n + 1 - i
    if j > (n + 1) / 2:
        j = n + 1 - j
    if i > j:
        s = j % 3
    else:
        s = i % 3
    if s == 0:
        s = 3
    print(s)