s = list(str(input()))
l = []
for i in range(26):
    l.append(-1)
n = -1
for i in s:
    n += 1
    if l[ord(i) - 97] == -1:
        l[ord(i) - 97] = n
for i in l:
    print(i, end=" ")