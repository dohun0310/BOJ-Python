r = int(input())
for i in range(r - 1):
    if i == 0:
        print(" " * (r - 1) + "*")
    else:
        print(" " * (r - i - 1) + "*" + " " * (2 * i - 1) + "*")
print("*" * (2 * r - 1))