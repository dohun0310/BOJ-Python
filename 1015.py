n = int(input())
a = list(map(int, input().split()))
s = sorted(a)
p = [0] * n
for i in range(n):
    p[i] = s.index(a[i])
    s[s.index(a[i])] = -1
print(*p, end=" ")