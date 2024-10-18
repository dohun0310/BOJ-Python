s = input()
d = {}
for i in range(0, len(s), 3):
    if s[i:i + 3] in d:
        d[s[i:i + 3]] += 1
    else:
        d[s[i:i + 3]] = 1
t = [i for i in d.values() if i != 1]
if len(t) == 0:
    p, k, h, t = 13, 13, 13, 13
    for i in d:
        if i[0] == "P":
            p -= 1
        elif i[0] == "K":
            k -= 1
        elif i[0] == "H":
            h -= 1
        else:
            t -= 1
    print(p, k, h, t)
else:
    print("GRESKA")