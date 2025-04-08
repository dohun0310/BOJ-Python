for i in range(int(input())):
    n = int(input())
    d = {}
    for j in range(n):
        a, b = input().split()
        if b in d:
            d[b].append(a)
        else:
            d[b] = [a]
    c = 1
    for j in d:
        c *= (len(d[j]) + 1)
    print(c - 1)