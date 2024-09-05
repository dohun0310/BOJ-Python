e, f, c = map(int, input().split())
n = (e + f) // c + (e + f) % c
m = (e + f) // c
while n // c:
    m += n // c
    n = n // c + n % c
print(m)