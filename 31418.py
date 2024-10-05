import sys
w, h, k, t = map(int, sys.stdin.readline().split())
s = 1
for i in range(k):
    x, y = map(int, sys.stdin.readline().split())
    s *= (min(w, x + t) - max(1, x - t) + 1) % 998244353
    s %= 998244353
    s *= (min(h, y + t) - max(1, y - t) + 1) % 998244353
    s %= 998244353
print(s)