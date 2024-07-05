n = int(input())
a = list(map(int, input().split()))
s = []
for i in range(n):
    m = min(a[i:])
    j = a.index(m, i)
    if i != j:
        s.append([i + 1, j + 1])
        a[i:j + 1] = a[i:j + 1][::-1]
print(len(s))
for i in s:
    print(i[0], i[1])