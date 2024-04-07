r = int(input())
for i in range(r):
    n = []
    a, b, c = map(int, input().split())
    for i in range(1, b + 1):
        for j in range(1, a + 1):
            n.append(j * 100 + i)
    print(n[c - 1])