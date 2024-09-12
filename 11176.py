for i in range(int(input())):
    e, n = map(int, input().split())
    c = 0
    for j in range(n):
        a = int(input())
        if a > e:
            c += 1
    print(c)