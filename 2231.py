n = int(input())
b = False
for i in range(1000000):
    l = []
    for j in range(len(str(i))):
        l.append(int(str(i)[j]))
    if i + sum(l) == n:
        print(i)
        b = True
        break
if b == False:
    print(0)