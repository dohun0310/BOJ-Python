n = int(input())
l = list(map(int, input().split()))
c = 0
s = 0
for i in range(n):
    s += l[i - i] * c
    c += l[i]
print(s)