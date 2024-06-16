N = int(input())
w = 2
l = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
c = 0
y = 2019
while y <= N:
    m = 0
    while m < 12:
        if (w + 12) % 7 == 5:
            c += 1
        if m == 1:
            if (y % 400 == 0) or (y % 100 != 0 and y % 4 == 0):
                d = 29
            else:
                d = 28
        else:
            d = l[m]
        w = (w + d) % 7
        m += 1
    y += 1
print(c)