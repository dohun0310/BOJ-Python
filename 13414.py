import sys
k, l = map(int, sys.stdin.readline().split())
d = {}
for i in range(l):
    h = sys.stdin.readline().rstrip().zfill(8)
    d[h] = i
d = sorted(d.items(), key=lambda x: x[1])
c = 0
for i in d:
    c += 1
    print(i[0])
    if c == k:
        break