l = []
l.append(int(input()))
l.append(input())
l.append(int(input()))
if l[1] == "*":
    print(l[0] * l[2])
else:
    print(l[0] + l[2])