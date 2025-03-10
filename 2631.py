n = int(input())
l = [int(input()) for i in range(n)]
d = [0] * n
for i in range(n):
    for j in range(i):
        if l[i] > l[j] and d[i] < d[j]:
            d[i] = d[j]
    d[i] += 1
print(n - max(d))