n = int(input())
s = input()
a = "ABC" * (n // 3) + "ABC"[:n % 3]
b = "BABC" * (n // 4) + "BABC"[:n % 4]
g = "CCAABB" * (n // 6) + "CCAABB"[:n % 6]
u, c, h = 0, 0, 0
for i in range(n):
    if s[i] == a[i]:
        u += 1
    if s[i] == b[i]:
        c += 1
    if s[i] == g[i]:
        h += 1
print(max(u, c, h))
if u == max(u, c, h):
    print("Adrian")
if c == max(u, c, h):
    print("Bruno")
if h == max(u, c, h):
    print("Goran")