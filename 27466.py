n = int(input())
l = []
d = {"2": 2, "0": 1, "1": 1}
for i in range(n):
    a, b = input().split()
    a = int(a)
    t = d.copy()
    for j in b:
        if j in t:
            t[j] -= 1
            if all(count <= 0 for count in t.values()):
                l.append((i + 1, a))
                break
if not l:
    print(0)
else:
    print(min(l, key=lambda x: x[1])[0])