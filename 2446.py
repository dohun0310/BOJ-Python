r = int(input())
l = []
for i in range(r - 1):
    l.append(" " * i + "*" * (2 * r - 2 * i - 1))
    print(" " * i + "*" * (2 * r - 2 * i - 1))
print(" " * (r - 1) + "*")
for i in reversed(l):
    print(i)