n = int(input())
c = "369"
s = 0
for i in range(1, n + 1):
    a = str(i)
    for j in c:
        s += a.count(j)
print(s)