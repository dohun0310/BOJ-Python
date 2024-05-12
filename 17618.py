import sys
n = int(sys.stdin.readline())
s = 0
for i in range(1, n + 1):
    a = 0
    b = i
    while b:
        a += b % 10
        b //= 10
    if i % a == 0:
        s += 1
print(s)