n = {
    "063": 0,
    "010": 1,
    "093": 2,
    "079": 3,
    "106": 4,
    "103": 5,
    "119": 6,
    "011": 7,
    "127": 8,
    "107": 9
}
m = {j: i for i, j in n.items()}
while True:
    t = input()
    if t == "BYE":
        break
    a, b = t.split("+")[0], t.split("+")[-1][:-1]
    c, d = "", ""
    for i in range(0, len(a), 3):
        c += str(n[a[i:i + 3]])
    for i in range(0, len(b), 3):
        d += str(n[b[i:i + 3]])
    r = str(int(c) + int(d))
    s = ""
    for i in r:
        s += m[int(i)]
    print(t + s)