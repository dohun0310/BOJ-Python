for i in range(int(input())):
    n = list(map(int, input().split()))
    a = sum(n[1:]) / n[0]
    s = 0
    for i in n[1:]:
        if i > a:
            s += 1
    print("{:.3f}%".format((s / n[0]) * 100))