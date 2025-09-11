n = int(input())
l = list(map(int, input().split()))
l.sort()
c = 0
t = 0
for i in range(n)[::-1]:
    if l[i] % 2:
        t += l[i]
    else:
        c += l[i]
    if t % 2 != 1:
        c += t
        t = 0
print(c)