n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
q = int(input())
for i in range(q):
    x = input().split()
    if x[0] == "row":
        k = int(x[1]) - 1
        v = int(x[2])
        for j in range(m):
            a[k][j] += v
    elif x[0] == "col":
        k = int(x[1]) - 1
        v = int(x[2])
        for j in range(n):
            a[j][k] += v
s = 0
z = float("inf")
y = float("-inf")
for i in range(n):
    for j in range(m):
        s += a[i][j]
        if a[i][j] < z:
            z = a[i][j]
        if a[i][j] > y:
            y = a[i][j]
print(s, z, y)