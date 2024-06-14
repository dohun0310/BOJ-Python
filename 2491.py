n = int(input())
l = list(map(int, input().split()))
a = [1] * n
b = [1] * n
for i in range(n - 1):
    if l[i + 1] >= l[i]:
        a[i + 1] += a[i]
for i in range(n - 1):
    if l[i + 1] <= l[i]:
        b[i + 1] += b[i]
print(max(max(a), max(b)))