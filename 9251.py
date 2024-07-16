n = input()
m = input()
l = [[0] * (len(m) + 1) for i in range(len(n) + 1)]
for i in range(1, len(n) + 1):
    for j in range(1, len(m) + 1):
        if n[i - 1] == m[j - 1]:
            l[i][j] = l[i - 1][j - 1] + 1
        else:
            l[i][j] = max(l[i - 1][j], l[i][j - 1])
print(l[len(n)][len(m)])