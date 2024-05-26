n = input()
s = 0
while len(n) > 1:
    s += 1
    r = 0
    for i in n:
        r += int(i)
    n = str(r)
print(s)
if int(n) % 3 == 0:
    print("YES")
else:
    print("NO")