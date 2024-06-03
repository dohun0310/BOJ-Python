import sys
for i in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    while True:
        s = 1
        if n == 0 or n == 1:
            print(2)
            break
        else:
            for j in range(2, int(n ** 0.5) + 1):
                if n % j == 0:
                    s = 0
                    break
            if s == 1:
                print(n)
                break
            else:
                n += 1