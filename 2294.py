n, k = map(int, input().split())
l = [0] * n
for i in range(n):
    l[i] = int(input())
s = [0] + [100001] * k
for i in l:
    for j in range(i, k + 1):
        s[j] = min(s[j], s[j - i] + 1)
print(s[k] if s[k] != 100001 else -1)