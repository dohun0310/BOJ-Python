n = int(input())
a = list(map(int, input().split()))
q = int(input())
l = []
for i in range(q):
    l.append(input().split())
s = []
for i in l:
    if i[0] == "1":
        l = int(i[1]) - 1
        r = int(i[2]) - 1
        k = int(i[3])
        c = 0
        for j in range(l, r + 1):
            if a[j] == k:
                c += 1
        s.append(c)
    elif i[0] == "2":
        l = int(i[1]) - 1
        r = int(i[2]) - 1
        for j in range(l, r + 1):
            a[j] = -1
print(*s, sep="\n")