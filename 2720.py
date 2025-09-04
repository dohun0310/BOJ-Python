for i in range(int(input())):
    c = int(input())
    l = [25, 10, 5, 1]
    s = [0, 0, 0, 0]
    for j in range(4):
        x = c // l[j]
        y = c % l[j]
        s[j] = x
        c = y
    print(*s)