while True:
    s = 0
    n = input()
    if n == "0":
        break
    s += (len(n) - (n.count("0") + n.count("1"))) * 3
    if "0" in n:
        s += n.count("0") * 4
    if "1" in n:
        s += n.count("1") * 2
    print(s + (len(n) + 1))