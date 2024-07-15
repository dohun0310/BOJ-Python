from collections import deque
l = input()
s = deque()
a, t = 0, 1
for i in range(len(l)):
    if l[i] == "(":
        s.append(l[i])
        t *= 2
    elif l[i] == "[":
        s.append(l[i])
        t *= 3
    elif l[i] == ")":
        if not s or s[-1] == "[":
            a = 0
            break
        if l[i - 1] == "(":
            a += t
        s.pop()
        t //= 2
    else:
        if not s or s[-1] == "(":
            a = 0
            break
        if l[i - 1] == "[":
            a += t
        s.pop()
        t //= 3
if s:
    a = 0
print(a)