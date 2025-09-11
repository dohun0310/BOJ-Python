n = int(input())
l = [1, 2] * (n // 2)
if n % 2:
    print(*l + [3])
else:
    print(*l)