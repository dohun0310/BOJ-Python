n = int(input())
l = [0.0] * n
for i in range(n):
    l[i] = float(input())
for i in range(1, n):
    l[i] = max(l[i], l[i] * l[i - 1])
print("{:.3f}".format(max(l)))