n = int(input())
s = [""] * n
for i in range(n):
    s[i] = input()
m = int(input())
a = [""] * m
for i in range(m):
    a[i] = input()
t = s.index("?")
if t == 0:
    x = ""
else:
    x = s[t - 1][-1]
if t == len(s) - 1:
    y = ""
else:
    y = s[t + 1][0]
for i in a:
    if (i[0] == x or not x) and (i[-1] == y or not y):
        if i not in s:
            print(i)