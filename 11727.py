n = int(input())
l = [0] * 1001
l[1], l[2] = 1, 3
for i in range(3, n + 1):
    l[i] = (l[i - 1] + 2 * l[i - 2]) % 10007
print(l[n])