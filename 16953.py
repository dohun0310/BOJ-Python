a, b = map(int, input().split())
c = 1
while a != b:
    c += 1
    s = b
    if b % 10 == 1:
        b //= 10
    elif b % 2 == 0:
        b //= 2
    if s == b:
        print(-1)
        break
else:
    print(c)