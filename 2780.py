import sys
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, -1, -1]]
o, p = [-1, 1, 0, 0], [0, 0, -1, 1]
m, t = 1234567, 1001
v = [[0] * 10 for i in range(t)]
for i in range(10):
    v[1][i] = 1
for i in range(1, t - 1):
    for j in range(10):
        if j == 0:
            x, y = 0, 3
        else:
            x, y = (j - 1) % 3, (j - 1) // 3
        for k in range(4):
            a, b = x + o[k], y + p[k]
            if -1 < a < 3 and -1 < b < 4 and l[b][a] > -1 :
                v[i + 1][l[b][a]] = (v[i + 1][l[b][a]] + v[i][j]) % m
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    print(sum(v[n]) % m)