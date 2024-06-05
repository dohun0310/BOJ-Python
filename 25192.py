l = set()
c = 0
for i in range(int(input())):
    s = input()
    if s != "ENTER":
        if s not in l:
            c += 1
            l.add(s)
    elif s == "ENTER":
        l.clear()
print(c)