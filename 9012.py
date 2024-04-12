n = int(input())
for i in range(n):
    s = list(input())
    a = 0
    for j in s:
        if j == "(":
            a += 1
        else:
            a -= 1
        if a < 0:
            print("NO")
            break
    if a == 0:
        print("YES")
    elif a > 0:
        print("NO")