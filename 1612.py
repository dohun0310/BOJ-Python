import sys
n = int(sys.stdin.readline())
if n == 1:
    print(1)
elif n % 2 == 0 or n % 5 == 0:
    print(-1)
else:
    a, b = 1, 1
    while a != 0:
        a += (a * 9 + 1) % n
        a %= n
        b += 1
    print(b)