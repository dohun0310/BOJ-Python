n = int(input())
l = [0] * n
for i in range(n):
    l[i] = int(input())
l.sort()
s = []
for i in l:
    s.append(i * n)
    n -= 1
print(max(s))