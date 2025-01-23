t, w = map(int, input().split())
l = [0] * (t + 1)
for i in range(t):
    l[i + 1] = int(input())
s = [[0] * (w + 1) for i in range(t + 1)]
for i in range(1, t + 1):
    if l[i] == 1:
        s[i][0] = s[i - 1][0] + 1
    else:
        s[i][0] = s[i - 1][0]
    for j in range(1, w + 1):
        if l[i] == 2 and j % 2 == 1:
            s[i][j] = max(s[i - 1][j - 1], s[i - 1][j]) + 1
        elif l[i] == 1 and j % 2 == 0:
            s[i][j] = max(s[i - 1][j - 1], s[i - 1][j]) + 1
        else:
            s[i][j] = max(s[i - 1][j - 1], s[i - 1][j])
print(max(s[t]))