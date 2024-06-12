n = int(input())
l = [0] * 301
for i in range(n):
    l[i] = int(input())
s = [0] * 301
s[0] = l[0]
s[1] = l[0] + l[1]
s[2] = max(l[0] + l[2], l[1] + l[2])
for i in range(3, n):
    s[i] = max(s[i - 2] + l[i], s[i - 3] + l[i - 1] + l[i])
print(s[n - 1])