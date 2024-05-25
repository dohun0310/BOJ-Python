import math
m = int(input())
n = int(input())
l = [i for i in range(m, n + 1)]
s = []
for i in l:
    if i / int(math.sqrt(i)) ** 2 == 1:
        s.append(i)
if len(s) == 0:
    print(-1)
else:
    print(sum(s))
    print(min(s))