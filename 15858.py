from decimal import Decimal, getcontext
getcontext().prec = 50
a, b, c = map(Decimal, input().split())
print(f"{a * b / c:.20f}")