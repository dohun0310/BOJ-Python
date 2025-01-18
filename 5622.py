n = input()
s = 0
for i in n:
    if i in ["A", "B", "C"]:
        s += 3
    elif i in ["D", "E", "F"]:
        s += 4
    elif i in ["G", "H", "I"]:
        s += 5
    elif i in ["J", "K", "L"]:
        s += 6
    elif i in ["M", "N", "O"]:
        s += 7
    elif i in ["P", "Q", "R", "S"]:
        s += 8
    elif i in ["T", "U", "V"]:
        s += 9
    elif i in ["W", "X", "Y", "Z"]:
        s += 10
print(s)