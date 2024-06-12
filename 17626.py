import math
n = int(input())
if int(math.sqrt(n)) == math.sqrt(n):
    print(1)
    exit()
for i in range(1, int(math.sqrt(n)) + 1):
    if n - i * i == int(math.sqrt(n - i * i)) ** 2:
        print(2)
        exit()
for i in range(1, int(math.sqrt(n)) + 1):
    for j in range(1, int(math.sqrt(n - i * i)) + 1):
        if math.sqrt(n - i ** 2 - j ** 2) == int(math.sqrt(n - i ** 2 - j ** 2)):
            print(3)
            exit()
print(4)