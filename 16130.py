for i in range(int(input())):
    n = input()
    s, t = 0, 0
    y, m = 0, 0
    for j in n:
        v = ord(j) - ord("A") + 10 if j >= "A" else ord(j) - ord("0")
        t += v
        if t // 10 == (t - v) // 10:
            continue
        if t // 10 > 4:
            y = 1
        elif t // 10 == 4:
            m = 1
        else:
            s += t // 10
        if y or m:
            break
    if y:
        print(str(s) + "(09)")
    elif m:
        print(str(s) + "(weapon)")
    else:
        print(str(s))