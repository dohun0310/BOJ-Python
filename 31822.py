c = input()[:5]
s = 0
for i in range(int(input())):
    a = input()[:5]
    if a == c:
        s += 1
print(s)