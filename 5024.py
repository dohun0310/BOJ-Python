n, p = map(int, input().split())
l = sorted(list(map(int, input().split())))
s = -1
for i in range(n):
    s = max(s, p * (i + 1) - l[i])
print(s + l[0])