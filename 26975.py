n = int(input())
l = sorted(map(int, input().split()), reverse=True)
a = 0
b = 0
for i, t in enumerate(l):
    c = t * (i + 1)
    if c >= a:
        a = c
        b = t
print(a, b)