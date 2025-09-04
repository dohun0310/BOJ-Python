t = int(input())
d = [300, 60, 10]
s = [0, 0, 0]
for i in range(3):
    x = t // d[i]
    y = t % d[i]
    s[i] = x
    t = y
if y != 0:
    print(-1)
    exit()
print(*s)