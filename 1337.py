n = int(input())
l = [0] * n
for i in range(n):
    l[i] = int(input())
l.sort()
s = []
for i in range(0, n):
    c = 0
    for j in range(l[i], l[i] + 5):
        if j not in l:
            c += 1
    s.append(c)
print(min(s))