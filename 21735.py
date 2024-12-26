def b(t, i, v):
    global s
    v += l[i]
    if t == m:
        s = max(s, v)
        return
    if i == n - 1:
        s = max(s,v)
        return
    if i + 1 < n:
        b(t + 1, i + 1, v)
    if i + 2 < n:
        b(t + 1, i + 2, v // 2)
n, m = map(int, input().split())
l = list(map(int, input().split()))
s = 0
b(1, 0, 1)
if n > 1:
    b(1, 1, 0)
print(s)