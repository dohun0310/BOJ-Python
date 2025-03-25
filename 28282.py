import sys
x, k = map(int, sys.stdin.readline().split())
s = list(map(int, sys.stdin.readline().split()))
l, r = [0] * 10001, [0] * 10001
for i in range(x):
    l[s[i]] += 1
for i in range(x, x * 2):
    r[s[i]] += 1
a = 0
for i in range(1, k + 1):
    if l[i] > 0:
        for j in range(1, k + 1):
            if i == j:
                continue
            a += l[i] * r[j]
print(a)