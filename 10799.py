n = input()
c = 0
s = []
for i in range(len(n)):
    if n[i] == "(":
        s.append("(")
    else:
        if n[i - 1] == "(":
            s.pop()
            c += len(s)
        else:
            s.pop()
            c += 1
print(c)