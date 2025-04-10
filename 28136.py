n = int(input())
l = list(map(int, input().split()))
c = 0
for i in range(n):
    if l[(i + 1) % n] <= l[i]:
        c += 1
print(c)