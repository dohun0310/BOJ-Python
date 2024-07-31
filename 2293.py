n, k = map(int, input().split())
l = [0] * n
for i in range(n):
    l[i] = int(input())
l.sort()
s = [1] + [0] * k
for i in l:
    for j in range(i, k + 1):
        s[j] += s[j - i]
print(s[k])