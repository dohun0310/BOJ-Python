n, k = map(int, input().split())
l = [i for i in range(1, n + 1)]
s = [0] * n
c = 0
for i in range(n):
    c += k - 1
    if c >= len(l):
        c %= len(l)
    s[i] = str(l.pop(c))
print("<", ", ".join(s), ">", sep="")