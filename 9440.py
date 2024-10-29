while True:
    n = list(map(int, input().split()))
    if n == [0]:
        break
    x, y = "", ""
    l = sorted(n[1:])
    for i in range(n[0]):
        if l[i] != 0:
            x, y = str(l[i]), str(l[i + 1])
            l.pop(i)
            l.pop(i)
            break
    for i in range(0, len(l), 2):
        x += str(l[i])
        if i + 1 < len(l):
            y += str(l[i + 1])
    print(int(x) + int(y))