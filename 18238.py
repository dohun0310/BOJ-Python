s = input()
p = 65
c = 0
for i in s:
    l = ord(i) - p
    r = p - ord(i)
    p = ord(i)
    if l < 0:
        l += 26
    if r < 0:
        r += 26
    c += min(l, r)
print(c)