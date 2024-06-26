d = {}
for i in range(int(input())):
    o, p = input().split()
    d[p] = o
r = ""
for i in input():
    r += d[i]
s, e = map(int, input().split())
print(r[s - 1:e])