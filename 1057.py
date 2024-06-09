n, a, b = map(int, input().split())
c = 0
while a != b:
    a -= a // 2
    b -= b // 2
    c += 1
print(c)