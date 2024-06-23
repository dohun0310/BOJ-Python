from math import comb
n, m, k = map(int, input().split())
c = 0
for i in range(k, m + 1):
    if n - m >= m - i:
        c += comb(m, i) * comb(n - m, m - i)
print(c / comb(n, m))