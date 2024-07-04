import math
m = map(int, input().split())
l = list(map(int, input().split()))
k = int(input())
n = sum(l)
t = math.comb(n, k)
s = 0
for i in l:
    s += math.comb(i, k)
print(s / t)