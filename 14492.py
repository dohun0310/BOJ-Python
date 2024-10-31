n = int(input())
a, b, c = [], [], 0
for i in range(n * 2):
    if i < n:
        a.append(input().split())
    else:
        b.append(input().split())
for i in range(n):
    for j in range(n):
        for k in range(n):
            if a[i][k] == "1" and b[k][j] == "1":
                c += 1
                break
print(c)