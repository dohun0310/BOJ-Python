n = int(input())
l = [1, 1, 0, 1, 1]
for i in range(5, n + 1):
    if l[i - 1] + l[i - 3] + l[i - 4] == 3:
        l.append(0)
    else:
        l.append(1)
if l[n]:
    print("SK")
else:
    print("CY")