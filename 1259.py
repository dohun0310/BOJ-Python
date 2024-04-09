while True:
    l = []
    s = input()
    for i in range(len(s)):
        l.append(s[i])
    m = l[::-1]
    if len(l) == 1 and l[0] == "0":
        break
    else:
        if l == m:
            print("yes")
        else:
            print("no")