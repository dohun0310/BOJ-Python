n = int(input())
l = [[600, 600], [1320, 1320]]
for i in range(n):
    s, e = input().split()
    x = int(s[:2]) * 60 + int(s[2:]) - 10
    y = int(e[:2]) * 60 + int(e[2:]) + 10
    l.append([x, y])
l.sort()
s = 0
t = 600
for i, j in l:
    s = max(s, i - t)
    t = max(t, j)
print(s)