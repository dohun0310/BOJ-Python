n = int(input())
a = list(map(int, input().split()))
o = list(map(int, input().split()))
x, y = int(1e9), -int(1e9)
l = [(1, a[0], o[0], o[1], o[2], o[3])]
while l:
    t, s, d, b, u, v = l.pop()
    if t == n:
        x = min(x, s)
        y = max(y, s)
    else:
        if d:
            l.append((t + 1, s + a[t], d - 1, b, u, v))
        if b:
            l.append((t + 1, s - a[t], d, b - 1, u, v))
        if u:
            l.append((t + 1, s * a[t], d, b, u - 1, v))
        if v:
            l.append((t + 1, int(s / a[t]), d, b, u, v - 1))
print(y)
print(x)