n = int(input())
f = [1, 1, 1]
for i in range(3, n):
    f.append(f[i - 1] + f[i - 3])
print(f[n - 1])