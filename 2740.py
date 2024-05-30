n, m = map(int, input().split())
a = [[0]] * n
for i in range(n):
    a[i] = list(map(int, input().split()))
m, k = map(int, input().split())
b = [[0]] * m
for i in range(m):
    b[i] = list(map(int, input().split()))
c = [[0 for _ in range(k)] for _ in range(n)]
for i in range(n):
    for j in range(k):
        for l in range(m):
            c[i][j] += a[i][l] * b[l][j]
for i in c:
    print(*i, end=" ")
    print()