a, t = map(int, input().split())
s = 10 + 2 * (25 - a + t)
if s < 0:
    print(0)
else:
    print(s)