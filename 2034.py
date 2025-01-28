n = int(input())
l = ["C", "X", "D", "X", "E", "F", "X", "G", "X", "A", "X", "B"]
s = [0] * n
for i in range(n):
    s[i] = int(input()) % 12
for i in range(65, 72):
    c = chr(i)
    t = l.index(c)
    x = True
    for j in s:
        t += j
        t %= 12
        if l[t] == "X":
            x = False
            break
    if x:
        print(c, l[t])