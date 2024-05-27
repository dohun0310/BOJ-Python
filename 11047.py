n, k = map(int, input().split())
l = [0] * n
for i in range(n):
    l[i] = int(input())
l.reverse()
c = 0
for i in l:
    c += k // i
    k %= i
print(c)