n, q = map(int, input().split())
l = list(map(int, input().split()))
for i in range(q):
    s = 0
    a, b = map(int, input().split())
    if a == b:
        print(0)
    else:
        for j in range(a, b):
           s += abs(l[j] - l[j - 1])
        print(s)