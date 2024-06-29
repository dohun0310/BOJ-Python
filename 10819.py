from itertools import permutations
n = int(input())
l = list(map(int, input().split()))
s = -1
for i in list(permutations(l, n)):
    t = 0
    for j in range(len(i) - 1):
        t += abs(i[j] - i[j - 1])
    if t > s:
        s = t
print(s)