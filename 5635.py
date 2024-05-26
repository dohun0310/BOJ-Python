n = int(input())
l = [""] * n
for i in range(n):
    l[i] = list(map(str, input().split()))
    l[i][1] = int(l[i][1])
    l[i][2] = int(l[i][2])
    l[i][3] = int(l[i][3])
l.sort(key=lambda x: (-x[3], -x[2], -x[1]))
print(l[0][0])
print(l[-1][0])