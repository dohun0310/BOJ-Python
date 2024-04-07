c, d, e, f, g, a, b, C = map(int, input().split())
l = [c, d, e, f, g, a, b, C]
ls = [c, d, e, f, g, a, b, C]
ls.sort()
lr = [c, d, e, f, g, a, b, C]
lr.sort()
lr.reverse()
if l == ls:
    print("ascending")
elif l == lr:
    print("descending")
else:
    print("mixed")