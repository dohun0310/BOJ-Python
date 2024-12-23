n = int(input())
a = sorted(map(int, input().split()))
b = sorted(map(int, input().split()))
s = 0
l, r = 0, n - 1
while 0 <= r and l < n:
    m, w = a[l], b[r]
    if (m < 0 < w) or (m > 0 > w):
        if m + w < 0:
            s += 1
            l += 1
            r -= 1
        else:
            r -= 1
    elif m < 0 and w < 0:
        l += 1
    elif 0 < m and 0 < w:
        r -= 1
print(s)