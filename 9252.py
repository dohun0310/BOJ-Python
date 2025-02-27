a = [0] + list(input())
b = [0] + list(input())
l = [[""] * len(b) for i in range(len(a))]
for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            l[i][j] = l[i - 1][j - 1] + a[i]
        else:
            if len(l[i - 1][j]) > len(l[i][j - 1]):
                l[i][j] = l[i - 1][j]
            else:
                l[i][j] = l[i][j - 1]
s = l[-1][-1]
print(len(s))
print(s)