n, m = map(int, input().split())
l = list(map(int, input().split()))
s = [0] * n
for i in range(n):
    if i < m:
        s[i] = 0
    else:
        s[i] = max(s[i - 1], s[i - m] + l[i])
print(s[-1])