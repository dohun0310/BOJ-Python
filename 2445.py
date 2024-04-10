r = int(input())
l = []
for i in range(1, r):
    print("*" * i + " " * (2 * r - 2 * i) + "*" * i)
    l.append("*" * i + " " * (2 * r - 2 * i) + "*" * i)
print("*" * (2 * r))
for i in reversed(l):
    print(i)