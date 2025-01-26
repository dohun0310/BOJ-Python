l = list(input())
s = 10
for i in range(1, len(l)):
    if l[i] == l[i - 1]:
        s += 5
    else:
        s += 10
print(s)