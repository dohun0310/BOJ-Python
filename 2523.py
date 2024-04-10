r = int(input())
l = []
for i in range(1, r):
    l.append("*" * i)
    print("*" * i)
print("*" * r)
for i in reversed(l):
    print(i)