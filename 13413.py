for i in range(int(input())):
    l = []
    n = int(input())
    a = input()
    b = input()
    for j in range(n):
        if a[j] != b[j]:
            l.append(a[j])
    if not l:
        print(0)
    elif l.count("B") >= l.count("W"):
        print(l.count("B"))
    else:
        print(l.count("W"))