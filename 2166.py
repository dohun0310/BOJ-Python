n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
l.append(l[0])
s = 0
for i in range(n):
    s += l[i][0] * l[i + 1][1] - l[i][1] * l[i + 1][0]
print(abs(s) / 2)