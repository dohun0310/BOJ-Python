n = int(input())
a = list(map(int, input().split()))
l = [1] * n
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            l[i] = max(l[i], l[j] + 1)
print(max(l))
t = max(l)
s = []
for i in range(n)[::-1]:
    if l[i] == t:
        s.append(a[i])
        t -= 1
print(*s[::-1])