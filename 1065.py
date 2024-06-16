n = int(input())
s = 0
for i in range(1, n + 1):
    if i < 100:
        s += 1
    if i >= 100:
        if int(str(i)[0]) - int(str(i)[1]) == int(str(i)[1]) - int(str(i)[2]):
            s += 1
print(s)