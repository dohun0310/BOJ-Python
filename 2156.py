n = int(input())
l = [0] * 10000
for i in range(n):
    l[i] = int(input())
s = [l[0], l[0] + l[1], max(l[0] + l[2], l[1] + l[2], l[0] + l[1])] + [0] * 9997
for i in range(3, n):
    s[i] = max(l[i] + s[i - 2], l[i] + l[i - 1] + s[i - 3], s[i - 1])
print(max(s))