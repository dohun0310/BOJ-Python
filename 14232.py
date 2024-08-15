k = int(input())
t = k
l = []
for i in range(2, k):
    if i * i > k:
        break
    while t % i == 0:
        l.append(i)
        t //= i
if t != 1:
    l.append(t)
print(len(l))
print(*l)