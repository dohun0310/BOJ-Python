n, m = map(int, input().split())
l = [0] * m
s = 0
for i in range(m):
    l[i] = list(map(int, input().split()))
l.sort()
for i in range(1, m)[::-1]:
    x, y = l[i]
    if x >= n:
        pass
    if x < n <= y:
        s += n - x
print(s)