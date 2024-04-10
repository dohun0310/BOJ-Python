l = []
m = []
for i in range(9):
    l.append(list(map(int, input().split())))
for i in l:
    m.append(max(i))
n = 0
s = max(m)
for i in range(9):
    if s not in l[i]:
        n += 1
    else:
        n += 1
        print(s)
        print(n, l[i].index(s) + 1)
        break