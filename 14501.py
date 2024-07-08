n = int(input())
d = [0] * n
for i in range(n):
    d[i] = list(map(int, input().split()))
s = [0] * (n + 1)
for i in range(n):
    for j in range(i + d[i][0], n + 1):
        if s[j] < s[i] + d[i][1]:
            s[j] = s[i] + d[i][1]
print(s[n])