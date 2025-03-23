n = int(input())
l = list(map(int, input().split()))
p = []
for i in range(n):
    if not l[i] in p:
        for j in range(2, l[i]):
            t = l[i] % j
            if t == 0:
                break
        else:
            p.append(l[i])
if len(p) == 0:
    print(-1)
else:
    r = 1
    for i in p:
        r *= i
    print(r)