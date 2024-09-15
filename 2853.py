l = []
for i in range(int(input())):
    l.append(int(input()))
s = 0
for i in range(1, len(l)):
    if l[i] == 0:
        continue
    t, c = 1, l[i] - l[0]
    for j in range(1, len(l)):
        if l[j] == 0:
            continue
        if l[j] % c == 1:
            t += 1
            l[j] = 0
    if t != 1:
        s += 1
print(s)