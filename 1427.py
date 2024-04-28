n = input()
l = []
for i in n:
    l.append(i)
l.sort(reverse=True)
print("".join(l))