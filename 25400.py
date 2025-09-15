n = int(input())
a = list(map(int, input().split()))
t = 0
for i in range(n):
    if t + 1 == a[i]:
        t += 1
print(n - t)