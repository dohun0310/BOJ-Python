a, b = map(int, input().split())
if a > b * 2 or a <= b:
    print("NO")
else:
    print("YES")
    print(a - b)
    for i in range(a - b - 1):
        print("aba")
    print("a", end="")
    for i in range(b - (a - b) + 1):
        print("ba", end="")