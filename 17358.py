n = int(input()) - 1
s = 1
for i in range(1, n + 1, 2)[::-1]:
    s *= i
print(s % 1000000007)