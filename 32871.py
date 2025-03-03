l = []
for i in range(int(input())):
    n, m = map(int, input().split())
    if n > m:
        n, m = m, n
    if n == 1:
        l.append("YES")
    elif (m - n) % 2 == 0:
        l.append("NO")
    else:
        l.append("YES")
print(*l, sep="\n")