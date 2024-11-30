from math import lcm
x, y = map(int, input().split())
a, b = lcm(x, y) // x, lcm(x, y) // y
for i in range(1, lcm(x, y) + 1):
    if i % a == 0 and i % b != 0:
        print("1", end="")
    elif i % a != 0 and i % b == 0:
        print("2", end="")
    elif i % a == 0 and i % b == 0:
        print("3", end="")