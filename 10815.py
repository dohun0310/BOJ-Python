n = int(input())
c = list(map(int, input().split()))
m = int(input())
v = list(map(int, input().split()))
d = {}
for i in range(n):
    d[c[i]] = 1
for i in range(m):
    if v[i] in d:
        print(1, end=" ")
    else:
        print(0, end=" ")