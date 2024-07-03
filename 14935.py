x = input()
while True:
    if int(x) == int(x[0]) * len(x):
        print("FA")
        break
    x = str(int(x[0]) * len(x))
else:
    print("NFA")