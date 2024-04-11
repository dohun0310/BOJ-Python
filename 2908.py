l = list(map(str, input().split()))
m = []
n = []
s = []
for i in l[0]:
    m.append(i)
for i in l[1]:
    n.append(i)
m.reverse()
n.reverse()
s.append(int(m[0]) * 100 + int(m[1]) * 10 + int(m[2]))
s.append(int(n[0]) * 100 + int(n[1]) * 10 + int(n[2]))
print(max(s))