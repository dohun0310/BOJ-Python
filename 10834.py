m = int(input())
c, s = 0, 0
for i in range(m):
    a, b, r = map(int, input().split())
    if i == 0:
        c = a * b
    else:
        c = int(c / a * b)
    if r == 1:
        s = 1 - s
print(s, c)