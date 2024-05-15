import sys
from math import factorial
while True:
    n = sys.stdin.readline().rstrip()
    if n == "0":
        break
    else:
        s = 0
        for i in range(1, len(n) + 1):
            s += int(n[len(n) - i]) * factorial(i)
        print(s)