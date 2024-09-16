a, b, c = map(int, input().split())
d, e = map(int, input().split())
s = [(a * (d ** 2)) - (a * d), (2 * a * d * e + b * d) - (b * d), ((a * (e ** 2))+ (b * e) + c) - (c * d + e)]
f = (s[1] ** 2) - (4 * s[0] * s[2])
if s[0] == 0:
    if s[1] != 0:
        print("Remember my character")
    elif s[0] == s[1] and s[1] == s[2] and s[2] == s[0] and sum(s) == 0:
        print("Nice")
    else:
        print("Head on")
elif f > 0:
    print("Go ahead")
elif f == 0:
    print("Remember my character")
elif f < 0:
    print("Head on")