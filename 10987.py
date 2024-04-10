a = input()
m = ["a", "e", "i", "o", "u"]
l = []
s = 0
for i in range(len(a)):
    l.append(a[i])
for i in l:
    if i in m:
        s += 1
print(s)