n = input()
for i in range(1, len(n)):
    a, b = 1, 1
    for j in n[:i]:
        a *= int(j)
    for j in n[i:]:
        b *= int(j)
    if a == b:
        print("YES")
        exit()
print("NO")