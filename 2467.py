n = int(input())
l = 0
r = n - 1
s = 2000000000
d = list(map(int, input().split()))
while l < r:
    v = d[l] + d[r]
    if abs(v) <= s:
        x = d[l]
        y = d[r]
        s = abs(v)
    if v <= 0:
        l += 1
    else:
        r -= 1
print(x, y)