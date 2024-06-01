from math import factorial
n = int(input())
f = [0] * 21
for i in range(20, -1, -1):
    f[20 - i] = factorial(i)
s = 0
for i in f:
    if s + i < n:
        s += i
    elif s + i == n:
        print("YES")
        exit()
print("NO")