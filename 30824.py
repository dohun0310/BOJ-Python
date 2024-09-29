import sys
f = [0, 1] + [0] * 77
for i in range(2, 79):
    f[i] = f[i - 1] + f[i - 2]
for i in range(int(sys.stdin.readline())):
    k, x = map(int, sys.stdin.readline().split())
    s = 0
    if k == 1:
        for j in range(1, 79):
            if f[j] == x:
                s = 1
                break
    elif k == 2:
        for j in range(1, 79):
            for l in range(1, 79):
                if f[j] + f[l] == x:
                    s = 1
                    break
            if s:
                break
    else:
        for j in range(1, 79):
            for l in range(1, 79):
                for m in range(1, 79):
                    if f[j] + f[l] + f[m] == x:
                        s = 1
                        break
                if s:
                    break
            if s:
                break
    if s:
        print("YES")
    else:
        print("NO")