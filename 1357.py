def rev(x):
    l = list(str(x))
    l.reverse()
    a = "".join(l)
    return int(a)
x, y = map(str, input().split())
print(rev(rev(x) + rev(y)))