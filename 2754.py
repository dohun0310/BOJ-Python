s = str(input())
n = 0
if s[0] == "A":
    n = 4.0
    if s[1] == "+":
        print(n + 0.3)
    elif s[1] == "0":
        print(n)
    else:
        print(n - 0.3)
elif s[0] == "B":
    n = 3.0
    if s[1] == "+":
        print(n + 0.3)
    elif s[1] == "0":
        print(n)
    else:
        print(n - 0.3)
elif s[0] == "C":
    n = 2.0
    if s[1] == "+":
        print(n + 0.3)
    elif s[1] == "0":
        print(n)
    else:
        print(n - 0.3)
elif s[0] == "D":
    n = 1.0
    if s[1] == "+":
        print(n + 0.3)
    elif s[1] == "0":
        print(n)
    else:
        print(n - 0.3)
else:
    print(0.0)