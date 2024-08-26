n, r = map(int, input().split())
s = 0
p = n - r
for i in range(1, int(p ** 0.5) + 1):
    if p % i == 0:
        if i > r:
            s += i
        if i * i != p and p // i > r:
            s += p // i
print(s)