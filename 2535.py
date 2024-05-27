n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
l.sort(key=lambda x: -x[2])
print(l[0][0], l[0][1])
print(l[1][0], l[1][1])
i = 2
if l[0][0] == l[1][0]:
    while l[0][0] == l[i][0]:
        i += 1
print(l[i][0], l[i][1])