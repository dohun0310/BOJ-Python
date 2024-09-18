n = int(input())
a = [0] + list(map(int, input().split())) + [0, 0]
m = [0] + [float("-inf")] * (n + 2)
for i in range(1, n + 3):
    if i >= 3:
        m[i] = max(m[i], m[i - 3] + (a[i - 2] + a[i - 1] + a[i]) * 2)
    m[i] = max(m[i], m[i - 1] + a[i])
print(int(m[n + 2]))