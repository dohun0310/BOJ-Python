d = input()
a = input()
b = input()
if d == "E":
    if a == "O." and b == ".P":
        print("T")
    elif a == ".P" and b == "I.":
        print("F")
    elif a == ".P" and b == "O.":
        print("Lz")
    else:
        print("?")
elif d == "W":
    if a == "P." and b == ".O":
        print("T")
    elif a == ".I" and b == "P.":
        print("F")
    elif a == ".O" and b == "P.":
        print("Lz")
    else:
        print("?")
elif d == "S":
    if a == ".O" and b == "P.":
        print("T")
    elif a == "I." and b == ".P":
        print("F")
    elif a == "O." and b == ".P":
        print("Lz")
    else:
        print("?")
elif d == "N":
    if a == ".P" and b == "O.":
        print("T")
    elif a == "P." and b == ".I":
        print("F")
    elif a == "P." and b == ".O":
        print("Lz")
    else:
        print("?")