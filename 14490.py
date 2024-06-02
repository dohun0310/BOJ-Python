import sys
import math
n, m = sys.stdin.readline().split(":")
print("%d:%d" %(int(n)//math.gcd(int(n), int(m)), int(m)//math.gcd(int(n), int(m))))