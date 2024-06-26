x, n = map(int, input().split())
if n != 1 and n % 2 == 1:
    print("ERROR")
elif (x < 0 and n == 1) or (x > 0 and n == 0):
    print("INFINITE")
elif x > 0 and n != 0 and n % 2 == 0:
    print((x + (n // 2) - 1) // (n // 2) - 1)
else:
    print("0")