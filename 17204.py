n, k = map(int, input().split())
l = [0] * n
for i in range(n):
    l[i] = int(input())
c, m = 0, 0
for i in range(n):
    if m != k:
        m = l[m]
        c += 1
    else:
        print(c)
        break
else:
    print(-1)