p = [1, 1] + [0] * 1499999
for i in range(2, int(len(p) ** 0.5) + 1):
    if not p[i]:
        for j in range(i + i, len(p), i):
            p[j] = 1
s = []
for i in range(2, len(p)):
    if not p[i]:
        s.append(i)
for i in range(int(input())):
    t = sum(map(int, input().split()))
    a = 1
    if t < 4:
        print("NO")
    elif t % 2 == 0:
        print("YES")
    else:
        if t - 2 > len(p):
            for j in s:
                if (t - 2) % j == 0:
                    print("NO")
                    a = 0
                    break
            if a:
                print("YES")
        else:
            if t - 2 in s:
                print("YES")
            else:
                print("NO")