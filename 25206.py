a = 0
b = 0
for i in range(20):
    s, h, n = input().split()
    h = float(h)
    g = 0.0
    if n == "A+":
        g = 4.5
    elif n == "A0":
        g = 4.0
    elif n == "B+":
        g = 3.5
    elif n == "B0":
        g = 3.0
    elif n == "C+":
        g = 2.5
    elif n == "C0":
        g = 2.0
    elif n == "D+":
        g = 1.5
    elif n == "D0":
        g = 1.0
    elif n == "F":
        g = 0.0
    if n != "P":
        a += h
        b += h * g
print("%.6f" % (b / a))