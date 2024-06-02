u = list(map(int, input().split()))
s = list(map(int, input().split()))
a, b = 0, 0
c = False
for i in range(9):
    a += u[i]
    if a > b:
        c = True
    b += s[i]
if a < b and c == True:
    print("Yes")
else:
    print("No")