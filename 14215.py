l = list(map(int, input().split()))
l.sort()
a, b, c = l
if a + b <= c:
    c = a + b - 1
print(a + b + c)