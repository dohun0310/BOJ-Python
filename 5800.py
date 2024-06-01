for i in range(1, int(input()) + 1):
    l = list(map(int, input().split()))
    print("Class", i)
    l = sorted(l[1:], reverse=True)
    g = []
    for i in range(len(l)):
        g.append(l[i - 1] - l[i])
    print(f"Max {max(l)}, Min {min(l)}, Largest gap {max(g)}")