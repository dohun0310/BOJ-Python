a = int(input())
b = int(input())
l = []
for i in range(a, b + 1):
    n = 0
    for j in range(1, i + 1):
        if i % j == 0:
            n += 1
    if n == 2:
        l.append(i)
if len(l) > 0:
    print(sum(l))
    print(min(l))
else:
    print(-1)