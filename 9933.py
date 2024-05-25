n = int(input())
l = [""] * n
for i in range(n):
    l[i] = input()
r = [""] * n
for i in range(len(l)):
    s = ""
    for j in l[i]:
        s = j + s
    r[i] = s
a = [""] * 2
for i in l:
    for j in r:
        if i == j:
            a[0], a[1] = len(str(i)), i[len(i) // 2]
print(*a)