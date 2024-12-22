for i in range(int(input())):
    n = int(input())
    l = [1] * 10
    for j in range(n - 1):
        for k in range(10):
            l[k] = sum(l[k:])
    print(sum(l))