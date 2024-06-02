n = int(input())
t = 0
p = []
while t < 110:
    t += 1
    for i in range(2, t + 1):
        if t % i == 0:
            if t == i:
                p.append(i)
            break
i = 0
while n >= p[i] * p[i + 1]:
    i += 1
print(p[i] * p[i + 1])