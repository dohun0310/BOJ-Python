v, k = map(int, input().split())
l = [0] * 505050
s = []
for i in range(v, 0, -1):
    if not l[i + k]:
        l[i] = 1
        s.append(i)
print(len(s))
print(*s, sep="\n")