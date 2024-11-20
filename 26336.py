for i in range(int(input())):
    t, g, f = map(int, input().split())
    print(t, g, f)
    s = set()
    for j in range(g, t, g):
        s.add(j)
    for j in range(f, t, f):
        s.add(j)
    print(len(s))