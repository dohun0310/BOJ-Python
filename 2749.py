n = int(input())
f = [0, 1]
for i in range(2, 1500000):
    f.append(f[i - 1] + f[i - 2])
    f[i] %= 1000000
print(f[n % 1500000])