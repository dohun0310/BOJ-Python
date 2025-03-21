def cbf(d, s):
    for i in range(len(d) - 1):
        if d[i] < 9 and d[i + 1] > 0:
            t = d.copy()
            t[i] += 1
            t[i + 1] -= 1
            if i == 0 and t[0] == 0:
                pass
            elif set(t) == s:
                return True
        if d[i] > 0 and d[i + 1] < 9:
            t = d.copy()
            t[i] -= 1
            t[i + 1] += 1
            if i == 0 and t[0] == 0:
                pass
            elif set(t) == s:
                return True
    return False

for i in range(3):
    a, b = input().split()
    x, y = list(map(int, a)), list(map(int, b))
    if set(x) == set(y):
        print("friends")
    elif cbf(x, set(y)) or cbf(y, set(x)):
        print("almost friends")
    else:
        print("nothing")