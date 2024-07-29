from itertools import combinations
n = int(input())
l = [[0, 0]] * n
s = 10 ** 9
for i in range(n):
    l[i] = list(map(int, input().split()))
for i in range(1, n + 1):
    for j in combinations(range(n), i):
        a, b = 1, 0
        for k in range(n):
            if k in j:
                a *= l[k][0]
                b += l[k][1]
        s = min(s, abs(a - b))
print(s)