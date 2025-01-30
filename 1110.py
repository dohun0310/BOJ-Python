n = int(input())
t = n
c = 0
while True:
    n = (n % 10) * 10 + (n // 10 + n % 10) % 10
    c += 1
    if n == t:
        break
print(c)