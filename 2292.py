r = int(input())
n = 1
for i in range(r):
    n += 6 * i
    if n >= r:
        print(i + 1)
        break