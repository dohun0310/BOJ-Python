from math import factorial
n = int(input())
for i in str(factorial(n))[::-1]:
    if i == "0":
        continue
    print(i)
    break