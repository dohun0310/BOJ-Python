for i in range(int(input())):
    n = int(input())
    h = list(map(int, input().split()))
    t = set()
    for j in range(n - 1):
        if h[j] == h[j + 1]:
            t.add(h[j])
    for j in range(n - 2):
        if h[j] == h[j + 2]:
            t.add(h[j])
    if t:
        print(*sorted(t))
    else:
        print(-1)