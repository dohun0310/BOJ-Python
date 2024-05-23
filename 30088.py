n = int(input())
l = [0]
for i in range(1, n + 1):
    t = sum(list(map(int, input().split()))[1:])
    l.append(t)
l.sort()
a = [0] * (n + 1)
b = [0] * (n + 1)
for i in range(1, n + 1):
    a[i] = a[i - 1] + l[i]
    b[i] = b[i - 1] + a[i]
print(b[-1])