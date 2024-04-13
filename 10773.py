r = int(input())
l = []
for i in range(r):
    n = int(input())
    if n == 0:
        l.pop()
    else:
        l.append(n)
print(sum(l))