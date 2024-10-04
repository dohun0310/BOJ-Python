n = int(input())
s = 0
for i in range(len(str(n))):
    t = n % 10
    n //= 10
    if t > 4:
        s += (t - 1) * (9 ** i)
    else:
        s += t * (9 ** i)
print(s)