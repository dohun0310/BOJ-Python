n = int(input())
l = list(map(int, input().split()))
p = 0
for i in range(n):
    c = 0
    for j in range(i + 1, n):
        if l[i] > l[j]:
            c += 1
        else:
            break
    p = max(p, c)
print(p)