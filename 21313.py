n = int(input())
s = [1, 2] * (n // 2)
if n % 2:
    s += [3]
print(*s)