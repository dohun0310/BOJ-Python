k = int(input())
b = list(map(int, input().split()))
s = 0
t = 0
for i in range(k):
    if t == 1 and b[i] % 2 == 0:
        t = 0
        s += 1
    elif t == 0 and b[i] % 2:
        t = 1
        s += 1
if b[0] % 2 == 0:
    print(s + 1)
else:
    print(s)