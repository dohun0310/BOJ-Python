n, m = map(int, input().split())
s = set()
l = [[]] * n
for i in range(n):
    t = input().split()
    a, b = t[:m], t[m]
    x, y = 0, 0
    for j in a:
        if j == ".":
            x += 1
        else:
            x = 0
        y = max(x, y)
    l[i] = [y, b]
    s.add(y)
print(len(s))
for i in l:
    print(*i)