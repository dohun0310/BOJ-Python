w = int(input())
n = int(input())
l = [0] * n
for i in range(n):
    l[i] = int(input())
s = []
c, a = 0, 0
for i in range(n):
    s.append(l[i])
    c += l[i]
    if len(s) > 4:
        c -= s.pop(0)
    if c > w:
        break
    a += 1
print(a)