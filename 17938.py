n = int(input())
p, t = map(int, input().split())
a, b, c, v = 1, 2, 0, 1
for i in range(2, t + 1):
    c = a
    a += b
    a %= 2 * n
    if b == 2 * n:
        v = -1
    elif b == 1:
        v = 1
    b += v
if a > c:
    if (c - 1) // 2 <= p - 1 <= (a - 1) // 2:
        print("Dehet YeonJwaJe ^~^")
    else:
        print("Hing...NoJam")
else:
    if (c - 1) // 2 <= p - 1 or p - 1 <= (a - 1) // 2:
        print("Dehet YeonJwaJe ^~^")
    else:
        print("Hing...NoJam")