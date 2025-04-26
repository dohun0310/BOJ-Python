import math
n = int(input())
s = str(n)
a = 0
for i in range(1, 10):
    c = 0
    for j in range(1, len(s) + 1):
        if int(str(i) * j) <= n:
            c = j
        else:
            break
    a += c
if n < 10:
    print(a + 1)
else:
    print(a + int(math.log10(n)))