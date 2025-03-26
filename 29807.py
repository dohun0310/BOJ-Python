t = int(input())
l = list(map(int, input().split())) + [0] * (5 - t)
s = 0
if l[0] > l[2]:
    s += (l[0] - l[2]) * 508
else:
    s += (l[2] - l[0]) * 108
if l[1] > l[3]:
    s += (l[1] - l[3]) * 212
else:
    s += (l[3] - l[1]) * 305
if l[4] > 0:
    s += l[4] * 707
print(s * 4763)