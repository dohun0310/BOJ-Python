n = int(input())
p = list(map(int, input().split()))
l = p
for i in range(0, n):
    for j in range(1, i + 1):
        l[i] = min(l[i], l[i - j] + p[j - 1])
print(l[n - 1])