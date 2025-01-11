import math
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
x, y = 1, 1
for i in a:
    x *= i
for i in b:
    y *= i
s = str(math.gcd(x, y))
if len(s) > 9:
    print(s[-9:])
else:
    print(s)