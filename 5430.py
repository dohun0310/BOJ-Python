for i in range(int(input())):
    p = input()
    n = int(input())
    l = list(input()[1:-1].split(","))
    if n == 0:
        l = []
    r = 0
    for j in p:
        if j == "R":
            r += 1
        else:
            if len(l) == 0:
                r = -1
                break
            if r % 2 == 0:
                l.pop(0)
            else:
                l.pop()
    if r == -1:
        print("error")
    else:
        if r % 2 == 1:
            l.reverse()
        print("[" + ",".join(l) + "]")