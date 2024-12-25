x, y = -1, -1
t = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    if x > a or y > b:
        t = 1
        continue
    x, y = a, b
print("yes" if t == 0 else "no")