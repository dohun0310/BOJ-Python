import sys
n, m = map(int, sys.stdin.readline().split())
l = []
for _ in range(n):
    l.append(sys.stdin.readline().strip())
l.sort()
a = 0
s = []
for i in range(m):
    t = sys.stdin.readline().strip()
    s.append(t)
s.sort()
i = 0
j = 0
while i < n and j < m:
    if l[i][:len(s[j])] == s[j]:
        a += 1
        j += 1
        continue
    elif l[i] > s[j]:
        j += 1
        continue
    elif l[i] < s[j]:
        i += 1
        continue
print(a)