l = [0] * 9
a = 0
b = 0
for i in range(9):
    l[i] = int(input())
for i in range(8):
    for j in range(i + 1, 9):
        if sum(l) - (l[i] + l[j]) == 100:
            a = l[i]
            b = l[j]
l.remove(a)
l.remove(b)
for i in sorted(l):
    print(i)