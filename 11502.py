t = int(input())
l = [0] * t
for i in range(t):
    l[i] = int(input())
for i in l:
    n = list(range(2, i + 1))
    f = 0
    s = []
    while len(n) != 0:
        m = n[0]
        s.append(m)
        c = 0
        while c < len(n):
            if n[c] % m == 0:
                n.pop(c)
                c -= 1
            c += 1
    for j in s:
        for k in s:
            for o in s:
                if j + k + o == i:
                    print(j, k, o)
                    f = 1
                    break
            if f:
                break
        if f:
            break
    if not f:
        print(0)