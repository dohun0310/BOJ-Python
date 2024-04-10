r = int(input())
for i in range(r):
    if i == 0:
        print(" " * (r - 1) + "*")
    else:
        print(" " * (r - i - 1) + "*" + " " * (2 * i - 1) + "*")