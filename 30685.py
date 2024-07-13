import sys
n = int(sys.stdin.readline())
v = []
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    v.append((a, (b - 1) >> 1))
v.sort()
m = float("inf")
for i in range(n - 1):
    d = v[i + 1][0] - v[i][0] - 1
    if v[i + 1][0] - v[i][0] - 1 < v[i][1] + v[i + 1][1]:
        if v[i][1] > d // 2 and v[i + 1][1] > d // 2:
            t = d // 2 + 1
        elif v[i][1] > d // 2:
            t = d - v[i + 1][1] + 1
        else:
            t = d - v[i][1] + 1
        if m > t:
            m = t
if m != float("inf"):
    print(m - 1)
else:
    print("forever")
