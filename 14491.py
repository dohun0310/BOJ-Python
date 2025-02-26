n = int(input())
s = ""
t = 0
while 9 ** t <= n:
    t += 1
for i in range(t)[::-1]:
    s += str(n // (9 ** i))
    n %= 9 ** i
print(s)