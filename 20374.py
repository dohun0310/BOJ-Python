import sys
from decimal import Decimal
s = Decimal(0.0)
try:
    while True:
        t = sys.stdin.readline()
        s += Decimal(t)
except:
    print(s)