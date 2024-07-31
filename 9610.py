a, b, c, d, t = 0, 0, 0, 0, 0
for i in range(int(input())):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        t += 1
    elif x > 0 and y > 0:
        a += 1
    elif x < 0 and y > 0:
        b += 1
    elif x < 0 and y < 0:
        c += 1
    else:
        d += 1
print(f"Q1: {a}\nQ2: {b}\nQ3: {c}\nQ4: {d}\nAXIS: {t}")