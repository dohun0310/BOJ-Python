n, k = map(int, input().split())
a = list(map(int, input().split()))
x, y = 0, max(a)
while x < y:
    m = (x + y) // 2
    c = 0
    for i in a:
        if i > m:
            c += i - m
    if c > k:
        x = m + 1
    else:
        y = m
print(x)