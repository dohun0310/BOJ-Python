n = int(input())
d = {}
for i in range(n):
    b = input()
    if b in d:
        d[b] += 1
    else:
        d[b] = 1
s = []
for i in d.items():
    if max(d.values()) == i[1]:
        s.append(i[0])
print(sorted(s)[0])