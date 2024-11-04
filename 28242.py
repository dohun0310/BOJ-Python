n = int(input())
a, b = [], []
for i in range(1, n + 1):
    if i ** 2 > n:
        break
    if n % i == 0:
        a.append(i)
        a.append(n // i)
for i in range(1, n + 3):
    if i ** 2 > n + 2:
        break
    if (n + 2) % i == 0:
        b.append(i)
        b.append((n + 2) // i)
for i in a:
    for j in b:
        c = n // i
        d = -(n + 2) // j
        if i * d + j * c == n + 1:
            print(i, j, c, d)
            exit()
print(-1)