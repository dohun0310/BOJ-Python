x = int(input())
l = 1
while x > l:
    x -= l
    l += 1
if l % 2 == 0:
    m = x
    j = l - x + 1
else:
    m = l - x + 1
    j = x
print(f"{m}/{j}")