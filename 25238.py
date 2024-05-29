a, b = map(int, input().split())
s = a * ((100 - b) / 100)
if s < 100.0:
    print(1)
else:
    print(0)