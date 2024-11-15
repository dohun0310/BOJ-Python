import sys
l = [0] * 1001
t, u = 0, 0
for i in range(int(sys.stdin.readline())):
    d, c = map(str, sys.stdin.readline().split())
    c = int(c)
    if d == "jinju":
        print(c)
        t = c
    elif c > 1000:
        u += 1
    else:
        l[c] += 1
for i in range(t + 1, 1001):
    u += l[i]
print(u)