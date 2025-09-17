s = input()
k, y = 0, 0
a, b = "KOREA", "YONSEI"
for i in s:
    if k == 5 or y == 6:
        break
    if i == a[k]:
        k += 1
    if i == b[y]:
        y += 1
if k == 5:
    print(a)
else:
    print(b)