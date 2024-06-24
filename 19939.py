n, k = map(int, input().split())
l = [0] * k
for i in range(k):
    l[i] += i + 1
    n -= i + 1
if n < 0:
    print(-1)
else:
    while n > 0:
        for i in range(k - 1, -1, -1):
            if n == 0:
                break
            l[i] += 1
            n -= 1
    print(l[-1] - l[0])