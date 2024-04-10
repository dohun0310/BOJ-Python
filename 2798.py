n, m = map(int, input().split())
l = list(map(int, input().split()))
s = []
for i in range(n - 2):
    for j in range(i + 1, n -1):
        for k in range(i + 2, n):
            if l[i] + l[j] + l[k] <= m:
                s.append(l[i] + l[j] + l[k])
print(max(s))