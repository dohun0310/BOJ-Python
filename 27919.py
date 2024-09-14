v = input()
u, d, p, c, a = 0, 0, 0, 0, 0
s = ""
for i in v:
    if i == "U":
        u += 1
        c += 1
    elif i == "C":
        u += 1
        c += 1
    else:
        d += 1
        p += 1
if d % 2 == 0:
    if u > d // 2:
        s += "U"
else:
    if u > d // 2 + 1:
        s += "U"
if d > 0:
    s += "DP"
if s == "":
    s += "C"
print(s)