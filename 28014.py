n = int(input())
l = list(map(int, input().split()))
s = [0] * n
for i in range(n):
    if s[i] == 1:
        continue
    for j in range(i, n - 1):
        if l[j] > l[j + 1]:
            s[j + 1] = 1
        else:
            break
print(s.count(0))