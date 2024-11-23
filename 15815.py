x = input()
l = []
for i in x:
    if i == "+":
        a = l.pop()
        b = l.pop()
        l.append(a + b)
    elif i == "*":
        a = l.pop()
        b = l.pop()
        l.append(a * b)
    elif i == "-":
        a = l.pop()
        b = l.pop()
        l.append(b - a)
    elif i == "/":
        a = l.pop()
        b = l.pop()
        l.append(b // a)
    else:
        l.append(int(i))
print(*l)