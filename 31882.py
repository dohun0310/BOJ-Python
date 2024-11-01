n = int(input())
s = input()
c, t = 0, 1
for i in s:
    if i == "2":
        c += t * (t + 1)
        t += 1
    else:
        t = 1
print(c // 2)