x = int(input())
s = [64, 32, 16, 8, 4, 2, 1]
c = 0
for i in s:
    if x >= i:
        c += 1
        x -= i
    if x == 0:
        break
print(c)