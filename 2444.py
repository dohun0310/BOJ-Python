r = int(input())
l = []
for i in range(2 * r - 1):
    if r - (i + 1) >= 0:
        l.append(" " * (r - (i + 1)) + "*" * (2 * i + 1))
for i in l:
    print(i)
for i in reversed(l[0:r - 1]):
    print(i)