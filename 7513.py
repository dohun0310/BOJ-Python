t = int(input())
for i in range(1, t + 1):
    m = int(input())
    l = [""] * m
    for j in range(m):
        l[j] = input()
    n = int(input())
    a = []
    for j in range(n):
        k = list(map(int, input().split()))
        s = ""
        for o in k[1:]:
            s += l[o]
        a.append(s)
    print(f"Scenario #{i}:")
    for j in a:
        print(j)
    print()