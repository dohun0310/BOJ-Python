n = int(input())
l = list(map(int, input().split()))
p = set()
for i in range(n - 1):
    for j in range(i + 1, n):
        a = (l[j] - l[i]) / (j - i)
        if a - int(a) == 0:
            b = l[j] - a * j
            p.add((a, b))
s = []
for (i, j) in p:
    c = 0
    for k in range(n):
        if l[k] != i * k + j:
            c += 1
    s.append(c)
print(min(s))