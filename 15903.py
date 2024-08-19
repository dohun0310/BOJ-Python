n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
for i in range(m):
    a[0] = a[1] = a[0] + a[1]
    a.sort()
print(sum(a))