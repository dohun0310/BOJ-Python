s = input()
t = 0
p = 0
for i in range(len(s)):
    if t == 0 and s[i] == "K":
        t = 1
        p += 1
    elif t == 1 and s[i] == "O":
        t = 2
        p += 1
    elif t == 2 and s[i] == "R":
        t = 3
        p += 1
    elif t == 3 and s[i] == "E":
        t = 4
        p += 1
    elif t == 4 and s[i] == "A":
        t = 0
        p += 1
print(p)