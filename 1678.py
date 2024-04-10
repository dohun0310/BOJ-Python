import math
n = math.factorial(int(input()))
s = []
a = 0
for i in range(len(str(n))):
    s.append(str(n)[i])
s.reverse()
for i in s:
    if i == '0':
        a += 1
    else:
        break
print(a)