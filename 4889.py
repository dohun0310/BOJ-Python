s = []
while True:
    l = []
    c = 0
    n = input()
    if "-" in n:
        break
    for i in n:
        if i == "{":
            l.append(i)
        else:
            if l:
                l.pop()
            else:
                c += 1
                l.append("{")
    s.append(c + len(l) // 2)
for i in range(len(s)):
    print(f"{i + 1}. {s[i]}")