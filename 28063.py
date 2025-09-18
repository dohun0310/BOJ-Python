n = int(input())
x, y = map(int, input().split())
c = 0
if x > 1:
    c += 1
if x < n:
    c += 1
if y > 1:
    c += 1
if y < n:
    c += 1
print(c)