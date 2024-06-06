n = int(input())
for i in range(n - 1):
    print("* " * i + "*" * (1 + 4 * (n - i - 1)) + " *" * i)
    print("* " * (i + 1) + " " * (1 + 4 * (n - i - 2)) + " *" * (i + 1))
print("* " * (2 * n - 1))
for i in range(n - 1):
    print("* " * (n - i - 1) + " " * (1 + 4 * i) + " *" * (n - i - 1))
    print("* " * (n - i - 2) + "*" * (1 + 4 * (i + 1)) + " *" * (n - i - 2))