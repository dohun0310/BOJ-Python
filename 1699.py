n = int(input())
l = [i for i in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, i):
        if j * j > i:
            break
        if l[i] > l[i - j * j] + 1:
            l[i] = l[i - j * j] + 1
print(l[n])