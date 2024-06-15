n = int(input())
l = [0] * n
for i in range(n):
    l[i] = int(input())
l.sort(reverse=True)
s = 0
for i in range(2, len(l), 3):
    s += l[i]
print(sum(l) - s)