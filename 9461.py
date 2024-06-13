for i in range(int(input())):
    n = int(input())
    l = [0] * 101
    l[1], l[2] = 1, 1
    for i in range(3, n + 1):
        l[i] = l[i - 2] + l[i - 3]
    print(l[n])