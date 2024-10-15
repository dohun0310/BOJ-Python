n = int(input())
t = 0
while n > 0:
    t = 0
    for i in 1, 2, 3, 4:
        for j in range(i):
            n -= 5
            if n <= 0:
                t += 5 + n
                break
            t += 5
        if n <= 0:
            break
        for j in range(i):
            n -= 5
            if n <= 0:
                t -= 5 + n
                break
            t -= 5
        if n <= 0:
            break
if t % 5:
    print(t // 5 + 1)
else:
    print(t // 5)