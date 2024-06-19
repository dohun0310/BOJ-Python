for i in range(int(input())):
    n = int(input())
    l = []
    for j in range(2, n + 1):
        c = 0
        while n % j == 0:
            c += 1
            n //= j
        if c:
            l.append([j, c])
    for j in l:
        print(*j)