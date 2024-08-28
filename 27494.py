import sys
n = int(sys.stdin.readline())
if n < 2023:
    print(0)
else:
    s = 0
    for i in range(2023, n + 1):
        x = str(i)
        if not {"0", "2", "3"}.issubset(set(x)):
            continue
        l = []
        for j in x:
            if j == "2" and len(l) in [0, 2]:
                l.append(j)
            elif j == "0" and len(l) == 1:
                l.append(j)
            elif j == "3" and len(l) == 3:
                s += 1
                break
    print(s)