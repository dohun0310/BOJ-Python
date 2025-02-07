import sys
n = int(sys.stdin.readline())
l = [list(map(int, input().split())) for i in range(n)]
s = [0] * n
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        s[i] |= l[i][j]
print(*s)