n = int(input())
c = 0
n, m = 0, 0
for i in input() :
    if i == "L":
        m += 1
    elif i == "R":
        if m > 0:
            c += 1
            m -= 1
        else:
            break
    elif i == "S":
        n += 1
    elif i == "K":
        if n > 0:
            c += 1
            n -= 1
        else:
            break
    else:
        c += 1
print(c)