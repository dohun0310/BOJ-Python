n, x = map(int, input().split())
l = list(map(int, input().split()))
t = sum(l[:x])
s = t
c = 1
for i in range(x, n):
    t += l[i]
    t -= l[i - x]
    if t > s:
        s = t
        c = 1
    elif t == s:
        c += 1
if s == 0:
    print("SAD")
else:
    print(s)
    print(c)