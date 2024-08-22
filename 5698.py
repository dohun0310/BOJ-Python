while True:
    s = input()
    if s == "*":
        break
    s = s.lower()
    l = s.split()
    c = l[0][0]
    for i in l:
        if i[0] != c:
            print("N")
            break
    else:
        print("Y")