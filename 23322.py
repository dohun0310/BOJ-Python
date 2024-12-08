n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
c, s = 0, 0
m = min(a)
for i in range(1, n):
    if a[i - 1] <= a[i] and m < a[i]:
        while a[i - 1] < a[i]:
            a[i] -= 1
            c += 1
        s += 1
print(c, s)