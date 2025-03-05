t = 1080
for i in range(10):
    d = int(input())
    if d == 1:
        t += 90
    elif d == 2:
        t += 180
    elif d == 3:
        t -= 90
t //= 90
t %= 4
if t == 0:
    print("N")
elif t == 1:
    print("E")
elif t == 2:
    print("S")
else:
    print("W")