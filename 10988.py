s = input()
l = []
for i in s:
    l.append(i)
if l == list(reversed(l)):
    print(1)
else:
    print(0)