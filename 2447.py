def d(n):
    if n == 1:
        return "*"
    s = d(n // 3)
    l = []
    for i in s:
        l.append(i * 3)
    for i in s:
        l.append(i + " " * (n // 3) + i)
    for i in s:
        l.append(i * 3)
    return l
for i in d(int(input())):
    print(i)