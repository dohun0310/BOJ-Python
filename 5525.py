n = int(input())
m = int(input())
s = input()
a, c, i = 0, 0, 0
while i < (m - 1):
    if s[i:i + 3] == "IOI":
        i += 2
        c += 1
        if c == n:
            c -= 1
            a += 1
    else:
        i += 1
        c = 0
print(a)