from decimal import Decimal, ROUND_DOWN
d = {"F": Decimal("0.00"), "D0": Decimal("1.00"), "D+": Decimal("1.50"), "C0": Decimal("2.00"), "C+": Decimal("2.50"), "B0": Decimal("3.00"), "B+": Decimal("3.50"), "A0": Decimal("4.00"), "A+": Decimal("4.50")}
n, x = map(Decimal, input().split())
c = [tuple(input().split()) for i in range(int(n) - 1)]
l = Decimal(input())
a = sum(Decimal(i) for i, j in c) + l
b = sum(Decimal(i) * d[j] for i, j in c)
for i in d:
    if ((b + l * d[i]) / a).quantize(Decimal("0.00"), rounding=ROUND_DOWN) > x:
        print(i)
        break
else:
    print("impossible")