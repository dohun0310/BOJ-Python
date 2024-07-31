c, s = 100, 100
for i in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        s -= a
    elif a < b:
        c -= b
print(f"{c}\n{s}")