n = int(input())
a, b = map(int, input().split())
if n < a + b:
    m = 2 * n - a - b
else:
    m = a + b
print(((1 << m) - 1) << (n - m))