n = int(input())
s = 0
while True:
    if n % 5 == 0:
        s += n // 5
        break
    else:
        n -= 2
        s += 1
    if n < 0:
        s = -1
        break
if n < 0:
    print(-1)
else:
    print(s)