import math
n = int(input())
if n == 0:
    print(0)
    exit()
t = math.ceil(math.log2(n))
print(t + 1)