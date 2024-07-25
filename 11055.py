n = int(input())
a = list(map(int, input().split()))
l = [a[0]] + [1] * (n - 1)
for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            l[i] = max(l[i], l[j] + a[i])
        else:
            l[i] = max(l[i], a[i])
print(max(l))