t = input().split("-")
l = []
for i in t:
    s = 0
    p = i.split("+")
    for j in p:
        s += int(j)
    l.append(s)
for i in range(1, len(l)):
    l[0] -= l[i]
print(l[0])