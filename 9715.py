for i in range(int(input())):
    r, c = map(int, input().split())
    l = [[0] * (c + 1)] + [[0] + [*map(int, input())] for j in range(r)]
    s = (r + 1) * (c + 1) - sum(j.count(0) for j in l)
    s += sum(sum(max(0, b - a) for a, b in zip(j, j[1:])) for j in l)
    s += sum(sum(max(0, b - a) for a, b in zip(j, j[1:])) for j in zip(*l))
    print(s * 2)