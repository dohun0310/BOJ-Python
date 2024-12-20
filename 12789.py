n = int(input())
l = list(map(int, input().split()))
s = []
t = 1
for i in l:
    s.append(i)
    while s and s[-1] == t:
        s.pop()
        t += 1
if s:
    print("Sad")
else:
    print("Nice")