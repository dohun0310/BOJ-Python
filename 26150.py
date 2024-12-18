n = int(input())
d = {}
l = [""] * n
for i in range(n):
    s, t, b = map(str, input().split())
    d[int(t)] = s[int(b) - 1]
for i in sorted(d.keys()):
    if d[i].islower():
        print(d[i].upper(), end="")
    else:
        print(d[i], end="")