n = input()
s = 0
for i in range(len(n) - 1):
    s += 9 * (10 ** i) * (i + 1)
s += ((int(n) - (10 ** (len(n) - 1))) + 1) * len(n)
print(s)