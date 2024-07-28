k = int(input())
l = [1] * 10000000
for i in range(2, int(10000000 ** 0.5) + 1):
    if l[i]:
        for j in range(i * i, 10000000, i):
            l[j] = 0
s = [i for i in range(2, 10000000) if l[i]]
print(s[k - 1])