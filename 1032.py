n = int(input())
l = []
for i in range(n):
    s = l.append(list(input()))
for i in range(len(l) - 1):
    for j in range(len(l[i + 1])):
        if l[0][j] != l[i + 1][j]:
            l[0][j] = "?"
print("".join(l[0]))