l = [0] * 8
for i in range(8):
    l[i] = int(input())
s = sorted(l)
print(sum(s[3:]))
g = [0] * 5
for i in range(5):
    g[i] = l.index(s[i + 3]) + 1
g.sort()
print(*g, end=" ")