l = list(map(int, input().split()))
l.sort()
if l[2] ** 2 == l[0] ** 2 + l[1] ** 2:
    print(1)
elif l.count(l[0]) == 3:
    print(2)
else:
    print(0)