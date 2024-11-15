l = [i for i in range(9, 1, -1)]
s = []
for i in range(int(input())):
    n = int(input())
    if n == 1:
        s.append(n)
    else:
        c = 0
        t = 0
        while True:
            if c == 8:
                s.append(-1)
                break
            if n == 1:
                s.append(t)
                break
            c = 0
            for j in range(8):
                if n % l[j] == 0:
                    n //= l[j]
                    t += 1
                    break
                else:
                    c += 1
for i in s:
    print(i)