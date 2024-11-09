n, m = map(int, input().split())
s, e = 0, 0
l = []
for i in range(n):
    a, b = map(int, input().split())
    l += [b] * a
for i in range(m):
    a, b = map(int, input().split())
    for j in range(e, e + a):
        if l[j] < b:
            s = max(s, b - l[j])
    e += a
print(s)