n, k = map(int, input().split())
l = list(map(int, input().split()))
t = 0
s = []
for i in l:
    t += i
    s.append(t)
r = s[k - 1]
for i in range(k, n):
    r = max(r, s[i] - s[i - k])
print(r)