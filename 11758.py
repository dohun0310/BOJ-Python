l = [[0, 0]] * 3
for i in range(3):
    l[i] = list(map(int, input().split()))
s = l[0][0] * l[1][1] + l[1][0] * l[2][1] + l[2][0] * l[0][1] - (l[1][0] * l[0][1] + l[2][0] * l[1][1] + l[0][0] * l[2][1])
if s > 0:
    print(1)
elif s < 0:
    print(-1)
else:
    print(0)