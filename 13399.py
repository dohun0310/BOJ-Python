n, m = map(int, input().split())
a, b = [0] * (m + 1), [0] * (n + 1)
for i in range(1, m + 1):
    a[i] = int(input())
for i in range(1, m + 1)[::-1]:
    if b[a[i]] == 0:
        print(a[i])
        b[a[i]] = 1
for i in range(1, n + 1):
    if b[i] == 0:
        print(i)