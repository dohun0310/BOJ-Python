n = int(input())
a = list(map(int, input().split()))
l = [1] * n
for i in range(n):
    t = 0
    x = i
    for j in range(i)[::-1]:
        if a[j] >= a[i] and l[j] > t:
            t = l[j]
            x = j
    if t != 0:
        a[i] += a[x]
        l[i] = t + 1
print(max(l))