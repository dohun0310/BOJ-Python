n = int(input())
l = list(map(str, input().split()))
t = {"B": 1, "S": 2, "G": 3, "P": 4, "D": 5}
a = [0] * n
s = []
for i in range(n):
    a[i] = t[l[i][0]] * 1000 + (1000 - int(l[i][1:]))
if a == sorted(a):
    print("OK")
else:
    print("KO")
    for i in range(n)[::-1]:
        if a[i] != sorted(a)[i]:
            s.append(l[i])
    print(*s)