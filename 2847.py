n = int(input())
c = 0
for i in range(n):
    l = list(input())
    s = []
    for j in l:
        if len(s) == 0:
            s.append(j)
        elif s[-1] == j:
            s.pop(-1)
        else:
            s.append(j)
    if len(s) == 0:
        c += 1
print(c)