n = int(input()) * 2
l = list(map(int, input().split()))
a = sorted(l)
b = sorted(l, reverse=True)
s = []
for i in range(n):
    s.append(a[i] + b[i])
print(min(s))