n = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = {}
for i in a:
    d[i] = 1
for i in b:
    if i in d:
        d[i] = 3
    else:
        d[i] = 2
l = sorted(d.keys())
x = 0
y = 0
z = 0
x = d[l[z]]
while x == 3 and z < len(l):
    z += 1
    if z < len(l):
        x = d[l[z]]
for i in range(z, len(l)):
    if x != d[l[i]] and d[l[i]] != 3:
        x = d[l[i]]
        y += 1
print(y)