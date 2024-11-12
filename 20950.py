import sys
sys.setrecursionlimit(1000000)
def dfs(t, num):
    global s, x, y, z
    if num >= 2:
        s = min(s, abs(x // num - r) + abs(y // num - g) + abs(z // num - b) )
    for i in range(t + 1, n):
        x, y, z = x + l[i][0], y + l[i][1], z + l[i][2]
        if num < 7:
            dfs(i, num + 1)
        x, y, z = x - l[i][0], y - l[i][1], z - l[i][2]
n = int(sys.stdin.readline())
l = [[*map(int, sys.stdin.readline().split())] for i in range(n)]
r, g, b = map(int, sys.stdin.readline().split())
x, y, z = 0, 0, 0
s = 99999999
dfs(-1, 0)
print(s)