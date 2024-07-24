n, l = map(int, input().split())
a, b, c = 0, 1, 0
while True:
    if str(l) not in str(b):
        a = b
        c += 1
    if c == n:
        break
    b += 1
print(a)