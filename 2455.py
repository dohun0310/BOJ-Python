n = 0
s = []
for i in range(4):
    l, b = map(int, input().split())
    n -= l
    n += b
    s.append(n)
print(max(s))