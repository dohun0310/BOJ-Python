n, k = map(int, input().split())
a = list(map(int, input().split(",")))
for i in range(k):
    b = [0] * (len(a) - 1)
    for i in range(len(a) - 1):
        b[i] = a[i + 1] - a[i]
    a = b
print(*a, sep=",")