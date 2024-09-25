x, y = -8140, -8140
c = 1
for i in range(29):
    x += 561
    y = -8140
    for j in range(29):
        if i == 0 and j == 0:
            pass
        elif i == 0 and j == 1:
            y += 560
        else:
            y += 561
        print(x, y)
        if c == 814:
            break
        c += 1
    if c == 814:
        break