n = int(input())
s = input()
a, b, c, h = 0, 0, 0, 0
for i in range(n):
    if s[i] == "D":
        a += 1
    elif s[i] == "K":
        b += a
    elif s[i] == "S":
        c += b
    elif s[i] == "H":
        h += c
print(h)