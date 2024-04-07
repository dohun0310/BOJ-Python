a = int(input())
b = int(input())
c = int(input())
l = list(str(a * b * c))
s = []
for i in l:
    s.append(i)
for i in range(10):
    print(s.count(str(i)))