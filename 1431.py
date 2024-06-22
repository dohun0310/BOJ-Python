def s(l):
    r = 0
    for i in l:
        if i.isdigit():
            r += int(i)
    return r
n = int(input())
l = [""] * n
for i in range(n):
    l[i] = input()
l.sort(key=lambda x:(len(x), s(x), x))
print(*l, sep="\n")