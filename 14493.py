n = int(input())
l = [[]] * n
c = 0
for i in range(n):
    l[i] = list(map(int, input().split()))
c += l[0][1]
i = 1
while i < n:
    c += 1
    if c % (l[i][0] + l[i][1]) >= l[i][1]:
        i += 1
    else:
        c += (l[i][1] - c % (l[i][0] + l[i][1]) - 1)
print(c + 1)