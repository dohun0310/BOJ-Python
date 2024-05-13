from collections import deque
n, k = map(int, input().split())
q = deque(range(1, n + 1))
s = []
while q:
    c = 1
    while c < k:
        i = q.popleft()
        q.append(i)
        c += 1
    i = q.popleft()
    s.append(i)
print("<", end="")
for i in s:
    if i == s[-1]:
        print(i, end="")
    else:
        print(i, end=", ")
print(">")