r = int(input())
for i in range(r):
    s = str(input())
    a = 0
    n = 0
    for i in s:
        if i == "O":
            a += 1
            n += a
        else:
            a = 0
            n += a
    print(n)