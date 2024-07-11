n = int(input())
if n & 1:
    n += 1
c = 1
for i in range(2, n + 1, 2):
    c *= i * (i - 1) // 2
    c //= i // 2
print(c)