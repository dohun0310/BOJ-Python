c = 0
for i in range(int(input())):
    n = input()
    if "01" in n or "OI" in n:
        c += 1
print(c)