l = []
for i in range(1, 31):
    l.append(i)
for i in range(28):
    n = int(input())
    l.remove(n)
l.sort()
print(l[0])
print(l[1])