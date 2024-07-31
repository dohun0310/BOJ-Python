for i in range(int(input())):
    l = list(input().split())
    n = float(l[0])
    for i in l[1:]:
        if i == "@":
            n *= 3
        elif i == "%":
            n += 5
        else:
            n -= 7
    print("{:.2f}".format(n))