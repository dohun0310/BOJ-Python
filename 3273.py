n = int(input())
l = sorted(list(map(int, input().split())))
x = int(input())
c = 0
a, b = 0, n - 1
while a < b:
    if l[a] + l[b] == x:
        c += 1
        a += 1
        b -= 1
    elif l[a] + l[b] < x:
        a += 1
    else:
        b -= 1
print(c)