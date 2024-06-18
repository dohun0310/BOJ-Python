while True:
    try:
        n = int(input())
    except:
        break
    i, c = 1, 1
    while True:
        if i % n != 0:
            i = i * 10 + 1
            c += 1
        else:
            break
    print(c)