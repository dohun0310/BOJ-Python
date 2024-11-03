n = int(input())
s = (n - 1) // 9 + 1
if s % 2 == 0 and n % 2 == 1:
    s += 1
print(s)