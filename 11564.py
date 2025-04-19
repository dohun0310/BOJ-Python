k, s, e = map(int, input().split())
if s == 0 or e == 0 or (s < 0 and e > 0):
    a = 1 + abs(s) // k + e // k
else:
    s, e = abs(s), abs(e)
    if s > e:
        s, e = e, s
    a = e // k - s // k
    if s % k == 0:
        a += 1
print(a)