n = int(input())
d = 1
c = 9
s = 1
while n > d * c:
    n -= d * c
    d += 1
    c *= 10
    s *= 10
print(str(s + (n - 1) // d)[(n - 1) % d])