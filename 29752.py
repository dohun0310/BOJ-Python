r = input()
l = list(map(int, input().split()))
n = 0
s = 0
for i in l:
    if i != 0:
        s += 1
        n = max(n, s)
    elif i == 0:
        n = max(n, s)
        s = 0
print(n)