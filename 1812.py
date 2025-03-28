n = int(input())
s = 0
l = [0] * n
for i in range(n):
    l[i] = int(input())
    s += l[i] * (-1) ** i
a = s // 2
print(a)
for i in range(n - 1):
    a = l[i] - a
    print(a)