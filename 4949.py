while True:
    t = input()
    l = []
    if t == ".":
        break
    for i in t:
        if i == "(" or i == "[":
            l.append(i)
        elif i == ")":
            if len(l) != 0 and l[-1] == "(":
                l.pop()
            else:
                l.append(")")
                break
        elif i == "]":
            if len(l) != 0 and l[-1] == "[":
                l.pop()
            else:
                l.append("]")
                break
    if len(l) == 0:
        print("yes")
    else:
        print("no")