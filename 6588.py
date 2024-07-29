import sys
l = [0] * 1000001
for i in range(2, int(1000001 ** 0.5) + 1):
    if not l[i]:
        for j in range(2 * i, 1000001, i):
            l[j] = 1
while True:
    n = int(sys.stdin.readline())
    if not n:
        break
    for i in range(3, n - 2, 2)[::-1]:
        if not l[i] and not l[n - i]:
            print(f"{n} = {n - i} + {i}")
            break
    else:
        print("Goldbach\'s conjecture is wrong.")