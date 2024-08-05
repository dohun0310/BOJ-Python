for i in range(int(input())):
    input()
    n, m = map(int, input().split())
    c = set(list(map(str, input().split())))
    h = set(list(map(str, input().split())))
    print(len(c.union(h)))