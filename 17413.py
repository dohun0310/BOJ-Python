from collections import deque
s = input()
l = deque()
a = ""
t = 0
for i in s:
    if i == "<":
        t = 1
        for j in range(len(l)):
            a += l.pop()
    l.append(i)
    if i == ">":
        t = 0
        for j in range(len(l)):
            a += l.popleft()
    if i == " " and t == 0:
        l.pop()
        for j in range(len(l)):
            a += l.pop()
        a += " "
if l:
    for i in range(len(l)):
        a += l.pop()
print(a)