import sys
from collections import deque
q = deque()
a, b, c = [], [], []
for i in range(int(sys.stdin.readline())):
    s = list(map(int, sys.stdin.readline().split()))
    if s[0] == 1:
        n = int(s[1])
        m = int(s[2])
        q.append((n, m))
    elif s[0] == 2:
        j = int(s[1])
        if q:
            n, m = q.popleft()
            if m == j:
                a.append(n)
            else:
                b.append(n)
while q:
    c.append(q.popleft()[0])
a.sort()
b.sort()
c.sort()
print(" ".join(map(str, a)) if a else "None")
print(" ".join(map(str, b)) if b else "None")
print(" ".join(map(str, c)) if c else "None")