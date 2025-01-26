for i in range(int(input())):
    d = {}
    for j in range(int(input())):
        a, b = input().split()
        if a not in d:
            d[a] = int(b)
        else:
            d[a] += int(b)
    d = sorted(d, key=lambda x: d[x], reverse=True)
    print(d[0])