n = 1000 - int(input())
s = 0
for i in [500, 100, 50, 10, 5, 1]:
    c = n // i
    n %= i
    s += c
print(s)