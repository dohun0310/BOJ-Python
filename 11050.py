import sys
def f(n):
    if n == 0:
        return 1
    else:
        return n * f(n-1)
n, k = map(int, sys.stdin.readline().split())
print(f(n) // (f(k) * f(n - k)))