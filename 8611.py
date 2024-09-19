n = int(input())
p = 1
for i in range(2, 10):
    t = n
    m = ""
    while t >= i:
        m += str(t % i)
        t //= i
    m += str(t)
    if m == m[::-1]:
        p = 0
        print(i, m)
if str(n) == str(n)[::-1]:
    print(10, n)
elif p:
    print("NIE")