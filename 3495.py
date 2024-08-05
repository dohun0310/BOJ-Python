h, w = map(int, input().split())
m = [[]] * h
for i in range(h):
    m[i] = list(input())
s = 0
for i in range(h):
    l = 0
    for j in m[i]:
        if j == "/" or j == "\\":
            l += 1
        if l % 2 == 1 and j == ".":
            s += 1
    s += l // 2
print(s)