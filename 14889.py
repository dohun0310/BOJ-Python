import sys
def backtrack(a, t):
    global s
    if a == n // 2:
        x, y = 0, 0
        for i in range(n):
            for j in range(n):
                if v[i] and v[j]:
                    x += l[i][j]
                elif not v[i] and not v[j]:
                    y += l[i][j]
        s = min(s, abs(x - y))
        return
    else:
        for i in range(t, n):
            if not v[i]:
                v[i] = 1
                backtrack(a + 1, i + 1)
                v[i] = 0
n = int(sys.stdin.readline())
v = [0] * n
l = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
s = 1e9
backtrack(0, 0)
print(s)