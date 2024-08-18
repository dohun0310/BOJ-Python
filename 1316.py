n = int(input())
t = n
for i in range(n):
    a = input()
    for j in range(0, len(a) - 1):
        if a[j] == a[j + 1]:
            continue
        elif a[j] in a[j + 1:]:
            t -= 1
            break
print(t)