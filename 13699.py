n = int(input())
l = [0] * 36
l[0], l[1], l[2], l[3] = 1, 1, 2, 5
for i in range(4, n + 1):
    for j in range(i):
        l[i] += l[j] * l[i - j - 1]
print(l[n])