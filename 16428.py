a, b = map(int, input().split())
if a % b < 0:
    print((a // b) + 1)
    print((a % b) - b)
else:
    print(a // b)
    print(a % b)