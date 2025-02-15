h, w = map(int, input().split())
n = int(input())
l = [list(map(int, input().split())) for i in range(n)]
s = 0
for i in range(n):
    for j in range(i + 1, n):
        a, b = l[i]
        x, y = l[j]
        if (a + x <= h and max(b, y) <= w) or (max(a, x) <= h and b + y <= w):
            s = max(s, a * b + x * y)
        if (b + x <= h and max(a, y) <= w) or (max(b, x) <= h and a + y <= w):
            s = max(s, a * b + x * y)
        if (b + y <= h and max(a, x) <= w) or (max(b, y) <= h and a + x <= w):
            s = max(s, a * b + x * y)
        if (a + y <= h and max(b, x) <= w) or (max(a, y) <= h and b + x <= w):
            s = max(s, a * b + x * y)
print(s)