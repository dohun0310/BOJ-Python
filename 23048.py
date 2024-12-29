import math
l = [0] * 500001
k = 2
c = [0, 1] + [0] * 499999
for i in range(2, 500001):
    l[i] = i
for i in range(2, int(math.sqrt(500001)) + 1):
    if l[i] == 0:
        continue
    for j in range(i * i, 500001, i):
        l[j] = 0
n = int(input())
for i in range(2, n + 1):
    if l[i] != 0:
        c[i] = k
        if i <= math.sqrt(n):
            for j in range(i * i, n + 1, i):
                c[j] = k
        k += 1
print(k - 1)
print(*c[1:n + 1])