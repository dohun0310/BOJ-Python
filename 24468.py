l, n, t = map(int, input().split())
b = []
a = 0
for i in range(n):
    s, c = input().split()
    s = int(s)
    b.append([s, c])
for i in range(t):
    t = [[] for i in range(l + 1)]
    for j in range(n):
        s, c = b[j]
        if c == "R":
            if s == l:
                b[j] = [s - 1, "L"]
            else:
                b[j] = [s + 1, "R"]
        else:
            if s == 0:
                b[j] = [1, "R"]
            else:
                b[j] = [s - 1, "L"]
        c = b[j][0]
        t[c].append(j)
        if len(t[c]) == 2:
            a += 1
            for k in t[c]:
                if b[k][1] == "L":
                    b[k][1] = "R"
                else:
                    b[k][1] = "L"
print(a)