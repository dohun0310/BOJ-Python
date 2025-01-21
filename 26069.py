n = int(input())
l = ["ChongChong"]
t = False
for i in range(n):
    a, b = map(str, input().split())
    if "ChongChong" in [a, b]:
        t = True
    if t:
        if a in l or b in l:
            l.append(a)
            l.append(b)
print(len(set(l)))