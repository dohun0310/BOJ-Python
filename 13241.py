a, b = map(int, input().split())
s = a * b
while b:
    if a > b:
        a, b = b, a
    b %= a
print(s // a)