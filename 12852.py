import sys
n = int(sys.stdin.readline())
l = [0] * (n + 1)
for i in range(2, n + 1):
    l[i] = l[i - 1] + 1
    if i % 2 == 0 and l[i] > l[i // 2] + 1:
        l[i] = l[i // 2] + 1
    if i % 3 == 0 and l[i] > l[i // 3] + 1:
        l[i] = l[i // 3] + 1
print(l[n])
s = [n]
t = l[n] - 1
r = n
for i in range(n)[::-1]:
    if l[i] == t and (i + 1 == r or i * 2 == r or i * 3 == r):
        r = i
        s.append(i)
        t -= 1
print(*s)