n = int(input())
l = []
for i in range(n):
    a, b, c, d = input().split()
    l.append([a, int(b), int(c), int(d)])
l.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for i in l:
    print(i[0])