import math
n = int(input())
if math.sqrt(n) ** 2 < n:
    print(math.isqrt(n) + 1)
elif float(math.isqrt(n)) == math.sqrt(n):
    print(math.isqrt(n))
else:
    print(math.isqrt(n) + 1)