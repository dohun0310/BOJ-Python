x = int(input())
if x % 3 == 1:
    print("U")
elif x == 2 or x % 3 == 2:
    print("O")
else:
    print("S")