s = input()
n = int(input())
a = [""] * n
for i in range(n):
    a[i] = input()
a.sort()
m = 0
r = a[0]
for i in a:
    l, o, v, e = s.count("L") + i.count("L"), s.count("O") + i.count("O"), s.count("V") + i.count("V"), s.count("E") + i.count("E")
    t = ((l + o) * (l + v) * (l + e) * (o + v) * (o + e) * (v + e)) % 100
    if t > m:
        m = t
        r = i
print(r)