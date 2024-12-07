l = [0, 1, 2] + [0] * 999
for i in range(3, 1001, 1):
    l[i] = l[i - 1] + l[i - 2]
while True:
    a, b = map(int,input().split())
    if a == 0 and b == 0:
        break
    c = 0
    for i in range(1,1001,1):
        if a <= l[i] <= b:
            c += 1
    print(c)