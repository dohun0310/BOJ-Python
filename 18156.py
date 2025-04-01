n = int(input())
l = [""] * n
for i in range(n):
    l[i] = input()
t = 1
for i in range(n):
    p = l[i]
    if p.count("B") > n // 2 or p.count("W") > n // 2:
        t = 0
    if "BBB" in p or "WWW" in p:
        t = 0
if t == 1:
    for i in range(n):
        p = ""
        for j in range(n):
            p += l[j][i]
        if p.count("B") > n // 2 or p.count("W") > n // 2:
            t = 0
        if "BBB" in p or "WWW" in p:
            t = 0
print(t)