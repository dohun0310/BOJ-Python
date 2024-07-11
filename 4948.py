l = [1] * (123456 * 2 + 1)
for i in range(1, len(l)):
    if i == 1:
        continue
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            l[i] = 0
            break
while True:
    n = int(input())
    if n == 0:
        break
    c = 0
    for i in range(n + 1, 2 * n + 1):
        if l[i]:
            c += l[i]
    print(c)