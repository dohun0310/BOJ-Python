n, m = map(int, input().split())
h = list(map(int, input().split()))
a, b = 1, max(h)
while a <= b:
    c = (a + b) // 2
    s = sum([i - c for i in h if i > c])
    if s < m:
        b = c - 1
    else:
        a = c + 1
print(b)