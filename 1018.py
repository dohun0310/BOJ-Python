n, m = map(int, input().split())
c = [""] * n
for i in range(n):
    c[i] = input()
s = []
for i in range(n - 7):
    for j in range(m - 7):
        w = 0
        b = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if c[k][l] != "W":
                        w += 1
                    if c[k][l] != "B":
                        b += 1
                else:
                    if c[k][l] != "B":
                        w += 1
                    if c[k][l] != "W":
                        b += 1
        s.append(w)
        s.append(b)
print(min(s))