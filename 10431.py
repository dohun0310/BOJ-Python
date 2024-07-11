p = int(input())
for i in range(p):
    l = list(map(int, input().split()))
    c = 0
    for i in range(1, len(l) - 1):
        for j in range(i + 1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]
                c += 1
    print(l[0], c)