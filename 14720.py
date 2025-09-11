n = int(input())
l = list(map(int, input().split()))
c = 0
t = 0
for i in range(n):
    if t == 3:
        t = 0
    if l[i] == t:
        t += 1
        c += 1
print(c)