n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
b = sorted(list(map(int, input().split())))
s = 0
for i in range(n):
    s += a[i] * b[i]
print(s)