n = int(input().strip())
l = sorted(list(map(int, input().split())))
a, c, t = 0, 0, 0
for i in l:
    if c == 0:
        t = i
    c += 1
    if c == t:
        a += 1
        c = 0
if c != 0:
    a += 1
print(a)