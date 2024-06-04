a, p = map(int, input().split())
l = [a]
while True:
    c = 0
    for i in str(l[-1]):
        c += int(i) ** p
    if c in l:
        break
    l.append(c)
print(l.index(c))