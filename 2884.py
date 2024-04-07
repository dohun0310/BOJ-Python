a, b = map(int, input().split())
t = a * 60 + b - 45
if t // 60 < 0:
    h = 24 + t // 60
else:
    h = t // 60
m = t % 60
print(h, m)