import sys
while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    if 0 <= n <= 9:
        print(10 + n)
    else:
        l = []
        t = n
        for i in range(2, 10)[::-1]:
            while t % i == 0:
                l.append(i)
                t //= i
        if t > 1:
            print("There is no such number.")
        else:
            l.sort()
            print(*l, sep="")